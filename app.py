from gradio_client import Client
import streamlit as st
import os
import sys
from dotenv import load_dotenv
import path
from streamlit.components.v1 import html
load_dotenv()

st.set_page_config(page_title="Cheers! Open AI Doc-Chat Assistant", layout="wide")
st.subheader("Open AI Doc-Chat Assistant: Life Enhancing with AI!")

css_file = "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

hf_token=os.getenv('hf_token')

user_query=st.text_input("Enter your query here: ")
client = Client("https://binqiangliu-llama2-txt-gen.hf.space/")
if user_query !="" and not user_query.strip().isspace() and not user_query == "" and not user_query.strip() == "" and not user_query.isspace():
  result = client.predict(user_query, api_name="/predict")
  st.write("AI Reponse: "+result)
else:
  st.write("Enter your query first.")
  st.stop()
