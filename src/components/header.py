import streamlit as st
def header_home():
    
    logo_url = "https://pub-1f9b302966c1432cb7e60b324f799175.r2.dev/ChatGPT%20Image%20Jul%203%2C%202026%2C%2005_10_06%20PM.png"
    st.markdown(f""" 
    <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px"> <img src = '{logo_url}', style='height:100px;align:center';/>
    <h1 style: 'text-align:center; color:e8e3ff'>ATTEND AI</h1></div>
""",unsafe_allow_html=True)
    
def header_dashboard():
    
    logo_url = "https://pub-1f9b302966c1432cb7e60b324f799175.r2.dev/ChatGPT%20Image%20Jul%203%2C%202026%2C%2005_10_06%20PM.png"
    st.markdown(f""" 
    <div style="display:flex; align-items:center; justify-content:center; gap:10px> <img src = '{logo_url}', style='height:85px;align:center';/>
    <h2 style: 'text-align:center; color:5865f2'>ATTEND AI</h2></div>
""",unsafe_allow_html=True)