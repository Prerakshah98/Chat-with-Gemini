import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# 1. Page Configuration
st.set_page_config(page_title="My AI Assistant", page_icon="🤖")

# 2. Setup the API Key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("API Key not found! Please create a .env file.")
    st.stop()
client = genai.Client(api_key=API_KEY)

# 3. The Title
st.title("🤖 My First GenAI App")
st.write("I am using the **Gemini Flash** model. Ask me anything!")

# 4. Input Box
user_input = st.text_input("Type your question here:", placeholder="E.g., What is the capital of India?")

# 5. The Logic (Button Click)
if st.button("Generate Answer"):
    if user_input:
        with st.spinner("Thinking..."):
            try:
                # We use 'gemini-flash-latest' because we know it works for you
                response = client.models.generate_content(
                    model="gemini-flash-latest",
                    contents=user_input
                )
                
                # Display the answer
                st.success("Here is the answer:")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question first!")