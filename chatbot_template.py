import streamlit as st
import utils
import db

# if 'llm_initialized' not in st.session_state:
#       db.set_llm()

st.title("Ask Me Anything")

# Initialize session state for chat messages
if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = []
    st.session_state.chat_messages = [{"role":"system","content":"you are a helpful assistant"}]

# Initialize session state for prompt selection
if 'prompt_selection' not in st.session_state:
    st.session_state.prompt_selection = None

if 'direction' not in st.session_state:
    st.session_state.direction = None

def on_direction_change():
    st.session_state.direction = st.session_state.direction_pill
    st.session_state.direction_pill = None

if st.sidebar.button(label="clear chat", 
                       help="clicking this button will clear the whole history",
                       icon="🗑️"):
        st.session_state.prompt_selection = None
        st.session_state["chat_messages"] = [{"role":"system","content":"you are a helpful assistant"}]

col1, col2 = st.columns([.99,.01])

with col1:
    options = ["What is Jonathan last's job", "What are Jonathan's top skills ?", 
            "what is 1+1 equal to ?", "summarize quantum physics in 50 words max"]

    st.session_state.setdefault("direction", None)
    prompt_selection = st.pills("Prompt suggestions", options, selection_mode="single", 
                                label_visibility='hidden',on_change=on_direction_change, key="direction_pill")
    input_prompt = st.chat_input("Type your message here...")
    st.session_state.prompt_selection = input_prompt

    if st.session_state.direction is not None:
        with st.chat_message("user"):
                st.session_state.chat_messages.append({"role": "user", "content": st.session_state.direction})
                st.write(st.session_state.direction)
        with st.spinner("searching ..."):  
            with st.chat_message("assistant"):
                # r = f"you wrote `{st.session_state.direction}`"
                # r = utils.simple_completion(messages=st.session_state.chat_messages)
                r = utils.chat_completion(query= st.session_state.direction)
                st.write(r)
                st.session_state.chat_messages.append({"role": "assistant", "content": r})
        st.session_state.direction = None

    elif st.session_state.prompt_selection is not None:
        st.session_state.chat_messages.append({"role": "user", "content": st.session_state.prompt_selection})
        with st.chat_message("user"):
                st.write(str(st.session_state.prompt_selection))
        with st.spinner("searching ..."):  
            with st.chat_message("assistant"):
                # r = f"you wrote `{st.session_state.prompt_selection}`"
                # r = utils.simple_completion(messages=st.session_state.chat_messages)
                r = utils.chat_completion(query=st.session_state.prompt_selection)
                st.write(r)
                st.session_state.chat_messages.append({"role": "assistant", "content": r})
        st.session_state.prompt_selection = None
    # st.json(st.session_state)
    
with col2:
    pass
    # st.json(st.session_state)