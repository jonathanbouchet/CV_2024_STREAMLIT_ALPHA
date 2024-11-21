import streamlit as st
import base64
from logger import logger

logger.info("about page")

st.markdown("# About Me")
st.write(
    """Customer oriented data scientist with proven ability of delivering valuable insights via data analytics.                    
    7+ years of professional experience in developing cutting-edge machine learning solutions for insurance leaders"""
)

# st.json(st.session_state)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("assets/JB_pic.png", width=500)

with st.sidebar:
    st.text("You can find me at ")
    col1, col2, col3 = st.sidebar.columns(3)
    with col1:
        st.markdown(
            """<a href="https://www.linkedin.com/in/jonathanbouchet/">
            <img src="data:image/png;base64,{}" width="75">
            </a>""".format(base64.b64encode(open("assets/LI-In-Bug.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """<a href="https://www.kaggle.com/jonathanbouchet">
            <img src="data:image/png;base64,{}" width="75">
            </a>""".format(base64.b64encode(open("assets/kaggle.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """<a href="https://github.com/jonathanbouchet">
            <img src="data:image/png;base64,{}" width="75">
            </a>""".format(base64.b64encode(open("assets/github.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )