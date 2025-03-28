import os
import streamlit as st
from dotenv import load_dotenv

import vertexai
from vertexai.generative_models import GenerativeModel

load_dotenv()

vertexai.init(project=os.environ.get("PROJECT_ID"), location="us-central1")

model = GenerativeModel(model_name="gemini-1.5-flash-002", system_instruction="Only give me information about neighboring states. Nothing else.")


st.title("Find your neighboring states")

users_state = st.text_input("Enter your state")


# Section A: Add in your Vertex AI API call below
response = model.generate_content(
    f"Find the neighboring states to {users_state}."
)
# End of Section A




# Section B:  Output the results to the user below
# Check if the user has submitted input
if st.button("Find Neighbors"):
    if users_state:  # Ensure input is not empty
        response = model.generate_content(
            f"Find the neighboring states to {users_state}."
        )
        st.write("The neighboring states are:\n" + response.text)
    else:
        st.warning("Please enter a valid state.")
# End of Section B