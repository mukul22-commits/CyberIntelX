import streamlit as st
import sqlite3
import os
import sys
from difflib import SequenceMatcher

sys.path.append("processing")

from complaint_risk_score import calculate_risk

from processing.auto_assign_officer import (
    auto_assign_officer
)

from processing.case_timeline import (
    log_timeline
)


def complaint_form():

    st.header("📝 Victim Complaint Portal")

    name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email"
    )

    phone = st.text_input(
        "Phone Number"
    )

    state = st.text_input(
        "State"
    )

    category = st.selectbox(
        "Complaint Category",
        [
            "Phishing",
            "UPI Fraud",
            "Investment Scam",
            "Job Scam",
            "Identity Theft",
            "Cyber Bullying",
            "Other"
        ]
    )

    description = st.text_area(
        "Incident Description"
    )

    uploaded_file = st.file_uploader(
        "Upload Evidence",
        type=[
            "jpg",
            "jpeg",
            "png",
            "pdf",
            "mp4"
        ]
    )

    if st.button(
        "Submit Complaint"
    ):

        if uploaded_file is None:

            st.error(
                "Please upload evidence."
            )

            return

        conn = sqlite3.connect(
            "database/complaints.db"
        )

        cursor = conn.cursor()

        # =========================
        # Duplicate Email Check
        # =========================

        cursor.execute(
            """
            SELECT id
            FROM complaints
            WHERE email=?
            """,
            (email,)
        )

        email_match = cursor.fetchone()

        if email_match:

            st.warning(
                f"""
Potential Duplicate Detected

Reason:
Same Email

Existing Case ID:
{email_match[0]}
"""
            )

        # =========================
        # Duplicate Phone Check
        # =========================

        cursor.execute(
            """
            SELECT id
            FROM complaints
            WHERE phone=?
            """,
            (phone,)
        )

        phone_match = cursor.fetchone()

        if phone_match:

            st.warning(
                f"""
Potential Duplicate Detected

Reason:
Same Phone Number

Existing Case ID:
{phone_match[0]}
"""
            )

        # =========================
        # Description Similarity
        # =========================

        cursor.execute(
            """
            SELECT
                id,
                description
            FROM complaints
            """
        )

        existing_cases = cursor.fetchall()

        for case_id, old_desc in existing_cases:

            similarity = SequenceMatcher(
                None,
                description.lower(),
                str(old_desc).lower()
            ).ratio()

            if similarity > 0.80:

                st.warning(
                    f"""
Possible Duplicate Complaint

Existing Case:
{case_id}

Description Similarity:
{round(similarity * 100, 2)}%
"""
                )

                break

        # =========================
        # Save Evidence
        # =========================

        os.makedirs(
            "evidence",
            exist_ok=True
        )

        filepath = os.path.join(
            "evidence",
            uploaded_file.name
        )

        with open(
            filepath,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        # =========================
        # Risk Score
        # =========================

        risk_score = calculate_risk(
            description
        )

        # =========================
        # Logged-In Victim
        # =========================

        victim_username = (
            st.session_state.get(
                "username",
                ""
            )
        )

        # =========================
        # Save Complaint
        # =========================

        cursor.execute(
            """
            INSERT INTO complaints(
                name,
                email,
                phone,
                state,
                category,
                description,
                evidence_file,
                risk_score,
                victim_username
            )
            VALUES(
                ?,?,?,?,?,?,?,?,?
            )
            """,
            (
                name,
                email,
                phone,
                state,
                category,
                description,
                filepath,
                risk_score,
                victim_username
            )
        )

        conn.commit()

        complaint_id = cursor.lastrowid

        conn.close()

        # =========================
        # Auto Assign Officer
        # =========================

        assignment = auto_assign_officer(
            complaint_id
        )

        # =========================
        # Timeline Events
        # =========================

        log_timeline(
            complaint_id,
            "Complaint Created",
            victim_username
        )

        if (
            assignment
            and
            assignment.get(
                "assigned_username"
            )
        ):

            log_timeline(
                complaint_id,
                "Officer Assigned",
                assignment[
                    "assigned_username"
                ]
            )

        # =========================
        # Success Message
        # =========================

        officer_name = (
            assignment.get(
                "officer_name",
                "Not Assigned"
            )
            if assignment
            else "Not Assigned"
        )

        st.success(
            f"""
Complaint Submitted Successfully

Complaint ID:
{complaint_id}

Risk Score:
{risk_score}

Assigned Officer:
{officer_name}
"""
        )