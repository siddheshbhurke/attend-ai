import streamlit as st

LOGO_URL = "https://pub-1f9b302966c1432cb7e60b324f799175.r2.dev/ChatGPT%20Image%20Jul%203%2C%202026%2C%2005_10_06%20PM.png"


def header_home():
    st.markdown(
        f"""
        <div style="text-align:center; margin-top:30px; margin-bottom:25px;">
            <img src="{LOGO_URL}" width="130">
        </div>

        <h1 class="logo-title" align="center">
            ATTEND AI
        </h1>
        """,
        unsafe_allow_html=True,
    )


def header_dashboard():
    left, right = st.columns([1, 5], vertical_alignment="center")

    with left:
        st.image(LOGO_URL, width=110)

    with right:
        st.markdown(
            """
            <div style="display:flex; align-items:center; height:100%;">
                <h2 class="dashboard-title" style="margin:0;">
                    ATTEND AI
                </h2>
            </div>
            """,
            unsafe_allow_html=True,
        )