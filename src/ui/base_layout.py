import streamlit as st


def style_background_home():
    st.markdown("""
    <style>
        .stApp {
            background: #5865F2 !important;
        }

        .stApp div[data-testid="stColumn"] {
            background-color: #E0E3FF !important;
            padding: 2.5rem !important;
            border-radius: 5rem !important;
        }
    </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
    <style>
        .stApp {
            background: #E0E3FF !important;
        }
    </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Outfit:wght@100..900&display=swap" rel="stylesheet">

    <style>

        # #MainMenu,
        # footer,
        # header{
        #     visibility:hidden;
        # }

        .block-container{
            padding-top:1.5rem !important;
            padding-bottom:1rem !important;
            padding-left:3rem !important;
            padding-right:3rem !important;
            max-width:100%;
        }

        html,
        body,
        p,
        span,
        div,
        label{
            font-family:'Outfit', sans-serif;
        }

        .logo-title{
            font-family:'Climate Crisis', cursive !important;
            font-size:3.5rem !important;
            line-height:1.1 !important;
            margin:0 !important;
            color:#E8E3FF !important;
            text-align:center;
        }

        .dashboard-title{
            font-family:'Climate Crisis', cursive !important;
            font-size:2rem !important;
            line-height:1.1 !important;
            margin:0 !important;
            color:#5865F2 !important;
        }

        h3,
        h4,
        h5,
        h6{
            font-family:'Outfit', sans-serif;
        }

        button[kind="primary"]{
            border-radius:1.5rem !important;
            background-color:#5865F2 !important;
            color:white !important;
            padding:10px 20px !important;
            border:none !important;
            transition:transform 0.25s ease-in-out !important;
        }

        button[kind="primary"]:hover{
            transform:scale(1.05);
        }

        button[kind="secondary"]{
            border-radius:1.5rem !important;
            background-color:#EB459E !important;
            color:white !important;
            padding:10px 20px !important;
            border:none !important;
            transition:transform 0.25s ease-in-out !important;
        }

        button[kind="secondary"]:hover{
            transform:scale(1.05);
        }

        button[kind="tertiary"]{
            border-radius:1.5rem !important;
            background-color:#0A0A0A !important;
            color:white !important;
            padding:10px 20px !important;
            border:none !important;
            transition:transform 0.25s ease-in-out !important;
        }

        button[kind="tertiary"]:hover{
            transform:scale(1.05);
        }

        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox div[data-baseweb="select"]{
            border-radius:12px !important;
        }

        hr{
            margin-top:1rem;
            margin-bottom:1rem;
        }

    </style>
    """, unsafe_allow_html=True)