import streamlit as st
import db
import firebase_admin

st.set_page_config(layout="wide",
                   page_title="Jonathan's webpage",
                   menu_items={
                       'Report a bug': "https://github.com/jonathanbouchet",
                       'Get help':"https://github.com/jonathanbouchet",
                       'About': "Jonathan Bouchet webpage"
    })

# if 'db_initialized' not in st.session_state:
    #   st.session_state["db_initialized"] = False
    #   db.set_db()
    #   st.session_state["db_initialized"] = True

# if 'llm_initialized' not in st.session_state:
    #   st.session_state["llm_initialized"] = False
    #   db.set_llm()
    #   st.session_state["llm_initialized"] = True

about_page = st.Page("about.py", title="About Jonathan")
resume_page = st.Page("resume.py", title="My Resume")
portfolio_page = st.Page("portfolio.py", title="My Portfolio")
comment_page = st.Page("submit_comment_page.py", title="Comment")
chat_page = st.Page("chatbot_template.py", title="Ask Me Anything")

if __name__ == "__main__":
    if not firebase_admin._apps:
        db.set_db()
    db.set_llm()
    pg = st.navigation([about_page, resume_page, portfolio_page, comment_page, chat_page])
    pg.run()