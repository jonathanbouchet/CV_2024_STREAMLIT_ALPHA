This part of the project documentation focuses on the main `streamlit` page.
It uses `st.navigation` to define the different pages shown on the left sidebar

## structure of the app
### `main`
```py
about_page = st.Page("about.py", title="About Jonathan", icon="❓" )
resume_page = st.Page("resume.py", title="My Resume", icon="📑")
portfolio_page = st.Page("portfolio.py", title="My Portfolio", icon="🔢")
comment_page = st.Page("submit_comment_page.py", title="Comment", icon="🖊️")

if __name__ == "__main__":
    pg = st.navigation([about_page, resume_page, portfolio_page, comment_page])
    pg.run()
```
:::main

Each page follows the same structure that is to load the `markdown` content and display it

```py
with open("assets/publications.md", "r") as f:
    data = f.read()

st.markdown(f"""{data}""")
```

## Logger
There is a simple `logging` module to print out every time a page is selected, and in the case of the `subnmit_comment` page, every time a comment is submitted