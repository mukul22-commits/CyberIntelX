import streamlit as st

from processing.victim_registration import (
    register_victim
)


def victim_registration():

    st.subheader(
        "Victim Registration"
    )

    full_name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email"
    )

    mobile = st.text_input(
        "Mobile"
    )

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Register"
    ):

        result = register_victim(
            username,
            password,
            full_name,
            email,
            mobile
        )

        if "error" in result:

            st.error(
                result["error"]
            )

        else:

            st.success(
                "Registration Successful"
            )