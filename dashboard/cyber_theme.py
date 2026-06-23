import streamlit as st


def apply_cyber_theme():

    st.markdown(
        """
<style>

/* Background */

.stApp {
    background:
        linear-gradient(
            135deg,
            #050816 0%,
            #0A0F1F 50%,
            #050816 100%
        );
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #08111f,
            #0d1b2a
        );
    border-right:
        1px solid rgba(
            0,
            255,
            255,
            0.2
        );
}

/* Metric Cards */

div[data-testid="metric-container"] {

    background:
        rgba(
            15,
            23,
            42,
            0.7
        );

    border:
        1px solid rgba(
            0,
            255,
            255,
            0.25
        );

    border-radius:18px;

    padding:18px;

    backdrop-filter:blur(12px);

    box-shadow:
        0 0 20px rgba(
            0,
            255,
            255,
            0.15
        );

    transition:0.3s;
}

/* Hover */

div[data-testid="metric-container"]:hover {

    transform:
        translateY(-3px);

    box-shadow:
        0 0 30px rgba(
            0,
            255,
            255,
            0.35
        );
}

/* DataFrames */

[data-testid="stDataFrame"] {

    border-radius:18px;

    overflow:hidden;

    border:
        1px solid rgba(
            0,
            255,
            255,
            0.2
        );
}

/* Buttons */

.stButton button {

    width:100%;

    border-radius:14px;

    height:52px;

    border:
        1px solid rgba(
            0,
            255,
            255,
            0.3
        );

    background:
        rgba(
            15,
            23,
            42,
            0.8
        );

    color:white;

    font-weight:600;
}

.stButton button:hover {

    background:
        rgba(
            0,
            255,
            255,
            0.15
        );

    border:
        1px solid cyan;
}

/* Headers */

h1 {

    color:#00ffff;

    text-shadow:
        0 0 10px cyan;
}

h2,
h3 {

    color:#cfefff;
}

/* Alert Boxes */

div.stAlert {

    border-radius:15px;
}

/* Scrollbar */

::-webkit-scrollbar {

    width:10px;
}

::-webkit-scrollbar-thumb {

    background:#00ffff;

    border-radius:20px;
}

</style>
""",
        unsafe_allow_html=True
    )