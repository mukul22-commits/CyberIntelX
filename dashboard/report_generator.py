from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

import sqlite3


def generate_report(complaint_id):

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
        (complaint_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    filename = (
        f"reports/complaint_{complaint_id}.pdf"
    )

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Cyber Crime Investigation Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    labels = [
        "ID",
        "Name",
        "Email",
        "Phone",
        "State",
        "Category",
        "Description",
        "Evidence File",
        "Risk Score",
        "Created At",
        "Status"
    ]

    for label, value in zip(labels, row):

        content.append(
            Paragraph(
                f"<b>{label}</b>: {value}",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 6)
        )

    doc.build(content)

    return filename