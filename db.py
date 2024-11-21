from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin
import streamlit as st
import models
import openai

# @st.cache_resource
def set_llm() -> None:
    """set openai credentials
    :return _type_: _description_
    """
    if True:#not st.session_state["llm_initialized"]:
        print("in set_llm")
        config_llm = models.Settings()
        print(f"llm config: {config_llm}")
        config_llm_deserialized = config_llm.model_dump()
        st.session_state["openai_apikey"] = config_llm_deserialized["OPENAI_API_KEY"]
        st.session_state["openai_model_4o_mini"] = config_llm_deserialized["OPEN_AI_MODEL_4o_MINI"]
        st.session_state["openai_model_4o"] = config_llm_deserialized["OPEN_AI_MODEL_4o"]
        client = openai.OpenAI(api_key=st.session_state["openai_apikey"])
        st.session_state["client"] = client


# @st.cache_resource
def set_db() -> None:
    """set firebase credentials
    Retrieve the credentials needed to set up a firebase connection from Settings
    """
    # set Firestore Database credentials
    if True:#not st.session_state["db_initialized"]:
        print("in set_db")
        config_firebase = models.FirebaseSettings()
        print(f"firebase config: {config_firebase}")
        config_firebase_deserialized = config_firebase.model_dump()
        # print(f"firebase config deserialized: {config_firebase_deserialized}")

        credential_values = {
            "type": config_firebase_deserialized.get("type"),
            "project_id": config_firebase_deserialized.get("project_id"),
            "private_key_id": config_firebase_deserialized.get("private_key_id"),
            "private_key": config_firebase_deserialized.get("private_key"),
            "client_email": config_firebase_deserialized.get("client_email"),
            "client_id": config_firebase_deserialized.get("client_id"),
            "auth_uri": config_firebase_deserialized.get("auth_uri"),
            "token_uri": config_firebase_deserialized.get("token_uri"),
            "auth_provider_x509_cert_url": config_firebase_deserialized.get("auth_provider_x509_cert_url"),
            "client_x509_cert_url": config_firebase_deserialized.get("client_x509_cert_url"),
            "universe_domain": config_firebase_deserialized.get("universe_domain"),
        }
        cred = credentials.Certificate(credential_values)
        firebase_admin.initialize_app(cred)
        st.session_state["db_initialized"] = True


def write_to_db(payload: dict, collection_name: str) -> str:
    """_summary_

    :param dict payload: _description_
    :param str collection_name: _description_
    :return str: _description_
    """
    # if "db_initialized" not in st.session_state:
    #     print("here")
    #     set_db()
    # if st.session_state["db_initialized"]:
        # print(f"in write_to_db, payload: {payload}, db col: {collection_name}")
    try:
        db = firestore.client()
        doc_ref = db.collection(f"{collection_name}").document()  # create a new document.ID
        doc_ref.set(payload)  # add obj to collection
        db.close()
        return "comment submitted"
    except Exception as e:
        print(e)
        return e
    # else:
    #     print("database not initialized")