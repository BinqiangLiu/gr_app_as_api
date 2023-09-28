from gradio_client import Client
import streamlit as st
import os
from dotenv import 


user_query=st.text_input("Enter your query here: ")
hf_token=os.getenv('hf_token')
client = Client("https://binqiangliu-llama2-txt-gen.hf.space/")
result = client.predict(
				user_query,	# str in 'prompt' Textbox component
				api_name="/predict"
)

st.write("AI Reponse: "+result)
