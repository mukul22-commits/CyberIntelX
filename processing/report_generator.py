from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import sqlite3
import os


def generate_case_report(case_id):

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM complaints
        WHERE id=?
        """,
        (case_id,)
    )

    case = cursor.fetchone()

    conn.close()

    if not case:

        return None

    os.makedirs(
        "reports",
        exist_ok=True
    )

    report_path = (
        f"reports/case_{case_id}.pdf"
    )

    doc = SimpleDocTemplate(
        report_path
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "Cyber Investigation Report",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    labels = [

        "ID",
        "Name",
        "Email",
        "Phone",
        "State",
        "Category",
        "Description",
        "Evidence",
        "Risk Score",
        "Created",
        "Status",
        "Officer",
        "Priority",
        "Notes"

    ]

    for label, value in zip(
        labels,
        case[:14]
    ):

        story.append(
            Paragraph(
                f"<b>{label}</b>: {value}",
                styles["BodyText"]
            )
        )

    doc.build(story)

    return report_path