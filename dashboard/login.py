import streamlit as st

from processing.login_manager import (
    login_user
)


def login_page():

    st.title(
        "🛡 Cyber Intelligence Command Center"
    )

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login"
    ):

        role = login_user(
            username,
            password
        )

        if role:

            st.session_state[
                "logged_in"
            ] = True

            st.session_state[
                "username"
            ] = username

            st.session_state[
                "role"
            ] = role

            st.rerun()

        else:

            st.error(
                "Invalid Credentials"
            )