import streamlit as st
import pandas as pd
import sqlite3
import os

from processing.case_status_manager import (
    update_case_status
)

from processing.case_notes import (
    update_notes
)

from processing.chain_of_custody import (
    log_custody
)

from processing.case_timeline import (
    log_timeline
)


def officer_portal():

    st.title("👮 Officer Portal")

    username = st.session_state.get(
        "username",
        ""
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    # =====================================
    # ASSIGNED CASES
    # =====================================

    try:

        complaints = pd.read_sql(
            """
            SELECT *
            FROM complaints
            WHERE assigned_username=?
            """,
            conn,
            params=(username,)
        )

    except Exception:

        officer_name = (
            username.split("_")[0]
            if "_" in username
            else username
        )

        complaints = pd.read_sql(
            """
            SELECT *
            FROM complaints
            WHERE lower(officer_name)
            LIKE ?
            """,
            conn,
            params=(
                f"%{officer_name.lower()}%",
            )
        )

    st.subheader(
        "Assigned Cases"
    )

    if len(complaints) == 0:

        st.warning(
            "No assigned cases found"
        )

    else:

        display_columns = [
            "id",
            "victim_username",
            "name",
            "category",
            "risk_score",
            "priority",
            "status",
            "officer_name"
        ]

        display_columns = [
            col
            for col in display_columns
            if col in complaints.columns
        ]

        st.dataframe(
            complaints[display_columns],
            width="stretch"
        )

    st.markdown("---")

    # =====================================
    # INVESTIGATION WORKSPACE
    # =====================================

    st.subheader(
        "Investigation Workspace"
    )

    if len(complaints) > 0:

        case_id = st.selectbox(
            "Select Case",
            complaints["id"]
        )

        selected = complaints[
            complaints["id"] == case_id
        ].iloc[0]

        st.write(
            f"Victim: {selected['name']}"
        )

        st.write(
            f"Category: {selected['category']}"
        )

        st.write(
            f"Risk Score: {selected['risk_score']}"
        )

        st.write(
            f"Status: {selected['status']}"
        )

        st.write(
            f"Description: {selected['description']}"
        )

        status = st.selectbox(
            "Update Status",
            [
                "Pending",
                "Under Investigation",
                "Evidence Review",
                "Escalated",
                "Resolved",
                "Closed"
            ]
        )

        notes = st.text_area(
            "Investigation Notes",
            value=str(
                selected["investigation_notes"]
                if "investigation_notes" in selected
                and selected["investigation_notes"]
                else ""
            )
        )

        if st.button(
            "Save Investigation"
        ):

            update_case_status(
                case_id,
                status
            )

            update_notes(
                case_id,
                notes
            )

            # ==========================
            # Timeline Logs
            # ==========================

            log_timeline(
                case_id,
                f"Status Changed To {status}",
                username
            )

            log_timeline(
                case_id,
                "Investigation Notes Updated",
                username
            )

            st.success(
                "Case Updated Successfully"
            )

            st.rerun()

    st.markdown("---")

    # =====================================
    # EVIDENCE VIEWER
    # =====================================

    st.subheader(
        "Evidence Viewer"
    )

    evidence_id = st.number_input(
        "Complaint ID",
        min_value=1,
        key="evidence_view"
    )

    if st.button(
        "Load Evidence"
    ):

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT evidence_file
            FROM complaints
            WHERE id=?
            """,
            (evidence_id,)
        )

        result = cursor.fetchone()

        if result:

            filepath = result[0]

            # ==========================
            # Custody Log
            # ==========================

            log_custody(
                evidence_id,
                "Evidence Viewed",
                username
            )

            # ==========================
            # Timeline Log
            # ==========================

            log_timeline(
                evidence_id,
                "Evidence Viewed",
                username
            )

            st.write(
                f"Evidence File: {filepath}"
            )

            if (
                filepath
                and
                os.path.exists(filepath)
            ):

                extension = (
                    filepath
                    .split(".")[-1]
                    .lower()
                )

                if extension in [
                    "jpg",
                    "jpeg",
                    "png"
                ]:

                    st.image(
                        filepath,
                        width="stretch"
                    )

                else:

                    with open(
                        filepath,
                        "rb"
                    ) as file:

                        st.download_button(
                            "Download Evidence",
                            file,
                            file_name=os.path.basename(
                                filepath
                            )
                        )

            else:

                st.warning(
                    "Evidence file not found"
                )

        else:

            st.error(
                "Complaint not found"
            )

    conn.close()