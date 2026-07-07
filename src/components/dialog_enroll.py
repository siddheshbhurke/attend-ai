import time

import streamlit as st

from src.database.config import supabase
from src.database.db import enroll_student_to_subject


@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write("Enter the subject code provided by your teacher")

    join_code = st.text_input(
        "Subject Code",
        placeholder="Eg. CS101"
    )

    if st.button("Enroll Now", type="primary", width="stretch"):

        if not join_code:
            st.warning("Please enter a valid Subject Code")
            return

        # Find the subject with the entered code
        res = (
            supabase.table("subjects")
            .select("subject_id, name, subject_code")
            .eq("subject_code", join_code.strip())
            .execute()
        )

        if not res.data:
            st.error("Invalid Subject Code")
            return

        subject = res.data[0]
        student_id = st.session_state.student_data["student_id"]

        # Check if THIS student is already enrolled in THIS subject
        check = (
            supabase.table("subject_students")
            .select("*")
            .eq("subject_id", subject["subject_id"])
            .eq("student_id", student_id)
            .execute()
        )

        if check.data:
            st.warning("You are already enrolled in this subject.")
            return

        # Enroll the student
        enroll_student_to_subject(student_id, subject["subject_id"])

        st.success(f"Successfully enrolled in {subject['name']}!")
        time.sleep(1)
        st.rerun()