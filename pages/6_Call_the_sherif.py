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

"""

"""
st.markdown("### Je contacte mon élu")
txt = st.text_area(
    "",
    "",
)

if txt:
    st.success("Message envoyé à votre élu")
    st.page_link("pages/7_Sherif_saloon.py", label = "Parapheur", icon = "📖")
    




