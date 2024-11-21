import streamlit as st
import models
import db
from operator import itemgetter

COLLECTION_NAME = "DB_CHATS"

def load_simple_context():
    return """
1. Jonathan Bouchet's resume, curriculum vitae, education, technical skills
2. Jonathan Bouchet's past and current work experience
3. Jonathan Bouchet's data analysis, such as tools and techniques used for data analysis
4. Jonathan Bouchet's publications
"""

def load_context() -> str:
    """_summary_

    :param str context_path: _description_
    :return str: _description_
    """
    context_path = "./assets/jb_resume.md"
    with open(context_path, "r") as f:
        data = f.read()
        return data
    

def make_messages(query: str, context: str):
    """"""
    messages = [
            {"role":"system", "content":"you are an expert at classifying a user query and finding if it is on topic with the context provided"
            f"""
            ### CONTEXT
            {context}
            query: {query}

            ### INSTRUCTION
            - find if the query is on topic with the context
            - Use the ResponseModel pydantic model to output your result
    """}
    ]

    return messages

def get_topical_response(query: str, context: str):
    """_summary_

    :param str query: _description_
    :return _type_: _description_
    """
    messages = make_messages(query=query, context=context)
    response = st.session_state["client"].beta.chat.completions.parse(
        model=st.session_state["openai_model_4o"],
        response_format=models.ResponseModel,
        messages=messages)
    
    return response


def get_final_response(query: str, context: str) -> str:
    """

    :param str query: _description_
    :param str context: _description_
    :return str: _description_
    """
    system_message: str = f"""
    you are a helpful assistant answering queries about Jonathan Bouchet work experience and skills.
    2. query:
    {query}
    2. You are given his resume, curriculum vitae,portfolio as context
    {context}
    """
    messages=[
        {"role":"system", "content": system_message},
        {"role": "user", "content": query}]
    response = st.session_state["client"].chat.completions.create(
        model=st.session_state["openai_model_4o_mini"],
        temperature=0.0,
        messages=messages
    )
    res=db.write_to_db(payload=response, collection_name=COLLECTION_NAME)
    return response.choices[0].message.content


def chat_completion(query: str):
    """_summary_

    :param str query: _description_
    :return _type_: _description_
    """
    if 'client' not in st.session_state:
        db.set_llm()
    moderation_response = st.session_state["client"].moderations.create(
        model="omni-moderation-latest",
        input=query)
    # print(colored(moderation_response,"cyan"))
    flagged = moderation_response.results[0].flagged

    if not flagged:
        context = load_simple_context()
        topical_response = get_topical_response(query=query, context = context)
        # print(colored(f'is_on_topic: {topical_response}', 'cyan'))
        topical_response_json = topical_response.choices[0].message.parsed.model_dump()
        if topical_response_json["on_topic"]:
            context = load_context()
            final_answer = get_final_response(query=query, context=context)
            return final_answer
        else:
            current_topic = topical_response_json["topic"]
            return f"guardrails flagged: {current_topic}. I'm happy to help! However, I must politely point out that the query is not related to Jonathan Bouchet's work experience or resume"
    else:
        for category, category_score in zip(moderation_response.results[0].categories, moderation_response.results[0].category_scores):
            print(category, category_score)
            l = list(moderation_response.results[0].category_scores)
            m = max(l, key=itemgetter(1))
        return f"topic flagged:{m[0]}. I can't provide information or guidance on illegal or harmful activities."
    

def simple_completion(messages: list):
    res = st.session_state["client"].chat.completions.create(
        messages=messages,
        model=st.session_state["openai_model_4o_mini"],
        temperature=0)
    return res.choices[0].message.content

    
