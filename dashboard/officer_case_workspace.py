import streamlit as st
import sqlite3
import pandas as pd

from processing.case_status_manager import (
    update_case_status
)

from processing.case_notes import (
    update_notes
)


def officer_case_workspace():

    st.subheader(
        "Investigation Workspace"
    )

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    df = pd.read_sql(
        """
        SELECT *
        FROM complaints
        ORDER BY id DESC
        """,
        conn
    )

    conn.close()

    case_id = st.selectbox(
        "Select Case",
        df["id"]
    )

    selected = df[
        df["id"] == case_id
    ].iloc[0]

    st.write(
        selected
    )

    status = st.selectbox(
        "Status",
        [
            "Pending",
            "Under Investigation",
            "Evidence Review",
            "Escalated",
            "Closed"
        ]
    )

    notes = st.text_area(
        "Investigation Notes",
        value=str(
            selected[
                "investigation_notes"
            ]
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

        st.success(
            "Case Updated"
        )