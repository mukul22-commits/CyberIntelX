import sqlite3
import pandas as pd


def generate_daily_brief():

    conn = sqlite3.connect(
        "database/cybercrime.db"
    )

    try:

        threats = pd.read_sql(
            """
            SELECT title,
                   source,
                   threat_score
            FROM intelligence_data
            ORDER BY threat_score DESC
            LIMIT 15
            """,
            conn
        )

    except:

        threats = pd.DataFrame()

    conn.close()

    brief = []

    brief.append(
        "DAILY CYBER INTELLIGENCE BRIEF"
    )

    brief.append(
        "================================="
    )

    brief.append("")

    brief.append(
        f"Top Threats Identified: {len(threats)}"
    )

    brief.append("")

    brief.append(
        "TOP THREATS"
    )

    brief.append(
        "-----------"
    )

    brief.append("")

    if not threats.empty:

        for _, row in threats.iterrows():

            brief.append(
                f"[{row['source']}] "
                f"{row['title']} "
                f"(Score: {row['threat_score']})"
            )

    else:

        brief.append(
            "No threat intelligence available."
        )

    brief.append("")
    brief.append(
        "RECOMMENDED ACTIONS"
    )

    brief.append(
        "-------------------"
    )

    brief.append(
        "- Monitor active threat campaigns"
    )

    brief.append(
        "- Investigate repeated IOC activity"
    )

    brief.append(
        "- Review high-risk vulnerabilities"
    )

    brief.append(
        "- Monitor threat actor activity"
    )

    brief.append(
        "- Escalate critical incidents"
    )

    return "\n".join(
        brief
    )