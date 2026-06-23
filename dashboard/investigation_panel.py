import streamlit as st
import pandas as pd
import sqlite3
import os

from report_generator import generate_report
from timeline_logger import log_action
from evidence_hash import generate_hash
from ioc_extractor import extract_iocs
from case_summary import generate_case_summary


def investigation_panel():

    st.title("🕵️ Investigation Panel")

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    st.subheader("All Complaints")

    search_name = st.text_input(
        "Search by Victim Name"
    )

    filter_status = st.selectbox(
        "Filter by Status",
        [
            "All",
            "Pending",
            "Under Investigation",
            "Resolved",
            "Closed"
        ]
    )

    filtered = complaints.copy()

    if search_name:

        filtered = filtered[
            filtered["name"].str.contains(
                search_name,
                case=False,
                na=False
            )
        ]

    if filter_status != "All":

        filtered = filtered[
            filtered["status"] == filter_status
        ]

    display_columns = [
        "id",
        "name",
        "category",
        "risk_score"
    ]

    optional_cols = [
        "status",
        "officer_name",
        "priority"
    ]

    for col in optional_cols:
        if col in filtered.columns:
            display_columns.append(col)

    st.dataframe(
        filtered[display_columns],
        width="stretch"
    )

    st.markdown("---")

    st.subheader(
        "Update Investigation Status"
    )

    complaint_id = st.number_input(
        "Complaint ID",
        min_value=1
    )

    status = st.selectbox(
        "Update Status",
        [
            "Pending",
            "Under Investigation",
            "Resolved",
            "Closed"
        ]
    )

    officer = ""

    try:

        officer_conn = sqlite3.connect(
            "database/officers.db"
        )

        officer_df = pd.read_sql(
            "SELECT name FROM officers",
            officer_conn
        )

        officer_conn.close()

        officer_list = officer_df[
            "name"
        ].tolist()

        if len(officer_list) > 0:

            officer = st.selectbox(
                "Assign Officer",
                officer_list
            )

        else:

            st.warning(
                "No officers registered"
            )

    except Exception:

        st.warning(
            "officers.db not found"
        )

    priority = st.selectbox(
        "Priority",
        [
            "Low",
            "Medium",
            "High",
            "Critical"
        ]
    )

    notes = st.text_area(
        "Investigation Notes"
    )

    if st.button(
        "Update Status"
    ):

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE complaints
                SET
                status=?,
                officer_name=?,
                priority=?,
                investigation_notes=?
                WHERE id=?
                """,
                (
                    status,
                    officer,
                    priority,
                    notes,
                    complaint_id
                )
            )

            conn.commit()

            log_action(
                complaint_id,
                f"Status changed to {status}"
            )

            if officer:

                log_action(
                    complaint_id,
                    f"Assigned Officer: {officer}"
                )

            log_action(
                complaint_id,
                f"Priority set to {priority}"
            )

            st.success(
                "Complaint Updated Successfully"
            )

        except Exception as e:

            st.error(str(e))

    st.markdown("---")

    st.subheader(
        "Generate Investigation Report"
    )

    report_id = st.number_input(
        "Complaint ID for Report",
        min_value=1,
        key="report_id"
    )

    if st.button(
        "Generate PDF Report"
    ):

        pdf_file = generate_report(
            report_id
        )

        if pdf_file:

            st.success(
                f"Report Generated: {pdf_file}"
            )

        else:

            st.error(
                "Complaint Not Found"
            )

    st.markdown("---")

    st.subheader(
        "Evidence Viewer"
    )

    selected_id = st.number_input(
        "Complaint ID",
        min_value=1,
        key="evidence"
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
            (selected_id,)
        )

        result = cursor.fetchone()

        if result:

            filepath = result[0]

            st.write(filepath)

            if os.path.exists(filepath):

                file_hash = generate_hash(
                    filepath
                )

                st.code(file_hash)

                extension = (
                    filepath.split(".")[-1]
                    .lower()
                )

                if extension in [
                    "jpg",
                    "jpeg",
                    "png"
                ]:

                    st.image(filepath)

                else:

                    with open(
                        filepath,
                        "rb"
                    ) as file:

                        st.download_button(
                            "Download",
                            file,
                            file_name=os.path.basename(filepath)
                        )

            else:

                st.error(
                    "File not found"
                )

    st.markdown("---")

    st.subheader(
        "Case Timeline"
    )

    timeline_id = st.number_input(
        "Complaint ID for Timeline",
        min_value=1,
        key="timeline"
    )

    if st.button(
        "Load Timeline"
    ):

        try:

            timeline = pd.read_sql(
                """
                SELECT action,
                       created_at
                FROM case_timeline
                WHERE complaint_id=?
                ORDER BY created_at DESC
                """,
                conn,
                params=(timeline_id,)
            )

            st.dataframe(
                timeline,
                width="stretch"
            )

        except Exception as e:

            st.error(str(e))

    st.markdown("---")

    st.subheader(
        "IOC Analysis"
    )

    ioc_id = st.number_input(
        "Complaint ID for IOC",
        min_value=1,
        key="ioc"
    )

    if st.button(
        "Analyze IOCs"
    ):

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT description
            FROM complaints
            WHERE id=?
            """,
            (ioc_id,)
        )

        result = cursor.fetchone()

        if result:

            iocs = extract_iocs(
                result[0]
            )

            st.write("Emails")
            st.write(iocs["emails"])

            st.write("URLs")
            st.write(iocs["urls"])

            st.write("IPs")
            st.write(iocs["ips"])

            st.write("Domains")
            st.write(iocs["domains"])

    st.markdown("---")

    st.subheader(
        "AI Investigation Summary"
    )

    summary_id = st.number_input(
        "Complaint ID",
        min_value=1,
        key="summary"
    )

    if st.button(
        "Generate Case Summary"
    ):

        case_df = pd.read_sql(
            """
            SELECT *
            FROM complaints
            WHERE id=?
            """,
            conn,
            params=(summary_id,)
        )

        if len(case_df) > 0:

            case = (
                case_df.iloc[0]
                .to_dict()
            )

            summary = (
                generate_case_summary(
                    case
                )
            )

            st.text_area(
                "Summary",
                summary,
                height=350
            )

        else:

            st.error(
                "Complaint Not Found"
            )

    conn.close()