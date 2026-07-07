import time

import streamlit as st

from src.database.config import supabase
from src.database.db import enroll_student_to_subject


@st.dialog("Enroll in Subject")
def auto_enroll_dialog(subject_code):
    student_id = st.session_state.student_data['student_id']
    st.write("Subject code:", repr(subject_code))
    try:
        res = supabase.table("subjects").select("subject_id, name").eq("subject_code", subject_code).execute()
    except Exception as e:
        st.exception(e)
        st.stop()
    
    if not res.data:
        st.error("Subject Code not Found")
        if st.button("Close"):
            st.query_params.clear()
            st.rerun()

        return
    
    subject = res.data[0]

    check = (
            supabase.table("subject_students")
            .select("*")
            .eq("subject_id", subject["subject_id"])
            .eq("student_id", student_id)
            .execute()
        )
    
    if check.data: 
        st.info("You are already Enrolled")
        if st.button("Got it !!!"):
            st.query_params.clear()
            st.rerun()

        return
    
    st.markdown(f"Would you like to enroll in ** {subject['name']} **")


    col1,col2 = st.columns(2)

    with col1:
        if st.button("No thanks"):
            st.query_params.clear()
            st.rerun()
    
    with col2:
        if st.button("Yes enroll now", type = "primary", width = "stretch"):
            enroll_student_to_subject(student_id, subject['subject_id'])
            st.success("Joined Successfully !!!")
            st.query_params.clear()
            time.sleep(2)
            st.rerun()
