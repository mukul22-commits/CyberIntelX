import sqlite3
import pandas as pd
import networkx as nx
import re


def build_graph():

    conn = sqlite3.connect(
        "database/complaints.db"
    )

    complaints = pd.read_sql(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    G = nx.Graph()

    for _, row in complaints.iterrows():

        case_id = f"Case {row['id']}"

        G.add_node(
            case_id,
            node_type="case"
        )

        description = str(
            row["description"]
        )

        emails = re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            description
        )

        urls = re.findall(
            r"https?://[^\s]+",
            description
        )

        ips = re.findall(
            r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            description
        )

        upis = re.findall(
            r"\b[\w\.-]+@[a-zA-Z]+\b",
            description
        )

        iocs = set(
            emails + urls + ips + upis
        )

        for ioc in iocs:

            G.add_node(
                ioc,
                node_type="ioc"
            )

            G.add_edge(
                case_id,
                ioc
            )

    return G