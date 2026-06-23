import streamlit as st
import sqlite3
import pandas as pd

def officer_management():

    st.title("👮 Officer Management")

    conn = sqlite3.connect("database/officers.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS officers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
    """)

    conn.commit()

    officer_name = st.text_input("Officer Name")

    if st.button("Add Officer"):

        try:
            cursor.execute(
                "INSERT INTO officers(name) VALUES(?)",
                (officer_name,)
            )

            conn.commit()
            st.success("Officer Added")

        except:
            st.warning("Officer Already Exists")

    officers = pd.read_sql(
        "SELECT * FROM officers",
        conn
    )

    st.dataframe(officers)

    conn.close()