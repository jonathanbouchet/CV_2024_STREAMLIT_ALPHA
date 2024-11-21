import streamlit as st
from logger import logger

logger.info("portfolio page")

with open("assets/data_analysis.md", "r") as f:
    data_analysis = f.read()

with open("assets/apps.md", "r") as f:
    data_apps = f.read()

with open("assets/publications.md", "r") as f:
    data_pubs = f.read()

st.sidebar.markdown("""
- [Analysis](#analysis)                   
- [Apps](#apps)                  
- [Publications](#pubs)""", unsafe_allow_html=True)

st.header("Analysis", divider="red")
st.write(f"""{data_analysis}""")

st.header("Apps", divider="red")
st.write(f"""{data_apps}""")

st.header("Publications", divider="red")
st.write(f"""{data_pubs}""")
