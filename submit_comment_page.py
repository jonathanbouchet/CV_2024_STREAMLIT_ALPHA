import streamlit as st
from pydantic import BaseModel, EmailStr, Field, ValidationError
from datetime import datetime
import db
import models
from logger import logger

COLLECTION_NAME = "DB_COMMENTS"

logger.info("submit comment page")

if "formbtn_state" not in st.session_state:
    st.session_state.formbtn_state = False
    
st.subheader("Request / Feedback / Comments")
with st.form(key = 'user_info'):
    st.write('Some Information about you')

    name = st.text_input(label="Name", help="your name")
    email = st.text_input(label="Email",help="your email")
    comment = st.text_area(label="Input",help="your input")
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    submit_form = st.form_submit_button(label="Submit", help="Click to submit comment")
    # print(submit_form, type(submit_form))

    # Checking if all the fields are non empty
    if submit_form:
        try:
            submit_form_pydantic = models.Form(name=name, email=email, comment=comment, time=current_time)
            # st.write(submit_form_pydantic)
            payload = submit_form_pydantic.model_dump()
            print(payload)
            # st.json(payload)
            try:
                res = db.write_to_db(payload=payload, collection_name=COLLECTION_NAME)
                logger.info("comment submitted")
                # print(res)
            except Exception as e:
                print(e)
            st.success(f"{res}. Thank you very much. I'll reach out to you shortly")
        except ValidationError as e:
            errors = e.errors()
            print(errors)
            error_msg = ""
            for error in errors:
                error_msg += f"{error['msg']}\n"
            st.error(f"{error_msg}")