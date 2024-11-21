import streamlit as st
from logger import logger

logger.info("resume page")

with open("assets/work_exp.md", "r") as f:
    data_work = f.read()

with open("assets/education.md", "r") as f:
    data_edu = f.read()

with open("assets/technical_skills.md", "r") as f:
    data_skills = f.read()

st.sidebar.markdown("""
- [Experience](#experience)                   
- [Education](#education)                  
- [Skills](#skills)""", unsafe_allow_html=True)

st.header("Experience", divider="red")
st.write(f"""{data_work}""")

st.header("Education", divider="red")
st.write(f"""{data_edu}""")

st.header("Skills", divider="red")
st.write(f"""{data_skills}""")
