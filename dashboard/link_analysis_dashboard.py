import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from processing.graph_builder import (
    build_graph
)


def link_analysis_dashboard():

    st.title(
        "🔗 Link Analysis Graph"
    )

    G = build_graph()

    if len(G.nodes()) == 0:

        st.warning(
            "No graph data available."
        )

        return

    fig = plt.figure(
        figsize=(12, 8)
    )

    pos = nx.spring_layout(
        G,
        seed=42
    )

    nx.draw(
        G,
        pos,
        with_labels=True
    )

    st.pyplot(fig)

    st.success(
        f"Nodes: {len(G.nodes())} | Edges: {len(G.edges())}"
    )