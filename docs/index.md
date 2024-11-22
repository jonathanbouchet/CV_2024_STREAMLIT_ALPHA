# Project overview

This repo provides `streamlit` code used for my webpage.

There are 4 pages available:

- `about me`: quick intro
- `resume`: my current resume
- `portfolio`: some of my work
- `comments`: a comment section. It connects to Google Firebase where comments are stored
- `chatbot`: a chatbot to ask questiona about my CV, experience:
    - the chatbot has no RAG since the document size is not too large.
    - moderation guardrails
    - topical guardrails
    - memory through `st.session_state`
