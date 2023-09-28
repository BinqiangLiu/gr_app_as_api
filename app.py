from gradio_client import Client
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
hf_token=os.getenv('hf_token')
user_query=st.text_input("Enter your query here: ")
client = Client("https://binqiangliu-llama2-txt-gen.hf.space/")
result = client.predict(user_query, api_name="/predict")
st.write("AI Reponse: "+result)
