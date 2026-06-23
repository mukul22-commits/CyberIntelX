import streamlit as st

from processing.report_generator import (
    generate_case_report
)


def report_center():

    st.title(
        "📄 Investigation Report Center"
    )

    case_id = st.number_input(
        "Complaint ID",
        min_value=1
    )

    if st.button(
        "Generate Report"
    ):

        report = generate_case_report(
            case_id
        )

        if report:

            with open(
                report,
                "rb"
            ) as f:

                st.download_button(
                    "Download Report",
                    f,
                    file_name=(
                        f"case_{case_id}.pdf"
                    )
                )

        else:

            st.error(
                "Case not found"
            )