import streamlit as st
from logger import logger

logger.info("publications page")

with open("assets/publications.md", "r") as f:
    data = f.read()

st.markdown(f"""{data}""")