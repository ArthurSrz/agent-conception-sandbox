from openai import OpenAI
import streamlit as st
from streamlit_feedback import streamlit_feedback
import trubrics



with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="feedback_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/5_Chat_with_user_feedback.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.markdown("## La Métropole")

st.markdown(
    """
    <style>
    .bandeau {
        background-color: #39eab9;
        padding: 30px;
        text-align: center;
        color: white;
        font-size: 34px;
        font-weight: bold;
    }
    </style>
    <div class="bandeau">Bienvenue à Métropole</div>
    """,
    unsafe_allow_html=True
)

#main variables



#state variables
if "messages" not in st.session_state:
    st.session_state.messages = []
if "response" not in st.session_state:
    st.session_state["response"] = None

messages = st.session_state.messages
#layout 
col1, col2, col3 = st.columns([1, 3, 1])


with col2:
    prompt = st.text_input("","",placeholder="Qu'est-ce que la Métropole peut faire pour vous ?")


    if prompt:
        messages.append({"role": "system", "content": """A chaque demande tu poses une question à la personne 
                         si elle souhaite envoyer un message directement à l'elu élus de la Métropole en charge de 
                         la thématique à laquelle se requête est liée. Sa réponse est très courte, 2 phrases maximum.
                         Chaque réponse mentionne systématiquement le lien "Je contacte mon élu" ainsi qu'ils obtiendront une réponse sous 1 semaine.
                        """})
        messages.append({"role": "user", "content": prompt})
        #st.chat_message("user").write(prompt)
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        st.session_state["response"] = response.choices[0].message.content
        with st.chat_message("assistant"):
            messages.append({"role": "assistant", "content": st.session_state["response"]})
            st.write(st.session_state["response"])
        link = st.page_link("pages/6_Call_the_sherif.py", label = "**Je dialogue avec mes élus**", icon = "🗨️")
        



"""

"""



