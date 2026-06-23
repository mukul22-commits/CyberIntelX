import streamlit as st


def navigation_hub():

    st.subheader(
        "⚡ Operations Center"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        if st.button(
            "🚨 Case Command Center",
            width="stretch"
        ):

            st.session_state["page"] = (
                "Case Command Center"
            )

            st.rerun()

    with c2:

        if st.button(
            "🧠 Analyst Operations",
            width="stretch"
        ):

            st.session_state["page"] = (
                "Analyst Operations Center"
            )

            st.rerun()

    with c3:

        if st.button(
            "🌐 National Threat Wall",
            width="stretch"
        ):

            st.session_state["page"] = (
                "National Threat Wall"
            )

            st.rerun()

    with c4:

        if st.button(
            "🏛 Executive Situation Room",
            width="stretch"
        ):

            st.session_state["page"] = (
                "Executive Situation Room"
            )

            st.rerun()