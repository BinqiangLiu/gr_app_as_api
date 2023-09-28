from gradio_client import Client
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

hf_token=os.getenv('hf_token')

user_query=st.text_input("Enter your query here: ")
client = Client("https://binqiangliu-llama2-txt-gen.hf.space/")
if user_query !="" and not user_query.strip().isspace() and not user_query == "" and not user_query.strip() == "" and not user_query.isspace():
  result = client.predict(user_query, api_name="/predict")
  st.write("AI Reponse: "+result)
else:
  st.write("Enter your query first.")
  st.stop()
