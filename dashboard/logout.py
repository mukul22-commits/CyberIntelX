import streamlit as st

from processing.logout_manager import (
    logout_user
)


def logout_button():

    if st.sidebar.button(
        "🚪 Logout"
    ):

        logout_user(
            st.session_state[
                "username"
            ]
        )

        st.session_state.clear()

        st.rerun()