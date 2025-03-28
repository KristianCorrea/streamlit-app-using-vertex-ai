import os
import streamlit as st
from dotenv import load_dotenv

import vertexai
from vertexai.generative_models import GenerativeModel

load_dotenv()

st.title("Find your neighboring states")

users_state = st.text_input("Enter your state")

# Section A: Add in your Vertex AI API call below

# End of Section A

st.write("The neighboring states are:")

# Section B:  Output the results to the user below

# End of Section B