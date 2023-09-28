from gradio_client import Client
import streamlit as st

user_query=st.text_input("Enter your query here: ")

client = Client("https://binqiangliu-llama2-txt-gen.hf.space/")
result = client.predict(
				user_query,	# str in 'prompt' Textbox component
				api_name="/predict"
)

st.write("AI Reponse: "+result)
