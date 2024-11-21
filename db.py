from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin
import streamlit as st
import models


@st.cache_resource
def set_db() -> None:
    """set firebase credentials
    Retrieve the credentials needed to set up a firebase connection from Settings

    """
     # set Firestore Database credentials
    if not st.session_state["db_initialized"]:
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

    # firebase_admin.initialize_app(cred,  {"storageBucket": credential_values["storageBucket"]})


def write_to_db(payload: dict, collection_name: str) -> str:
    """_summary_

    :param dict payload: _description_
    :param str collection_name: _description_
    :return str: _description_
    """
    if st.session_state["db_initialized"]:
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
    else:
        print("database not initialized")