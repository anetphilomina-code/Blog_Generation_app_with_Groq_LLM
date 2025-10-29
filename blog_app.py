

from groq import Groq
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)

# Streamlit UI
st.set_page_config(page_title="AI Blog Generator", layout="centered")
st.title("📝 AI Blog Generator using Groq (Llama 3)")

# User input
topic = st.text_input("Enter a topic for your blog:")

# Generate blog when button clicked
if st.button("Generate Blog"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Generating blog..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",  
                messages=[
                    {"role": "system", "content": "You are a creative blog writer."},
                    {"role": "user", "content": f"Write a detailed, engaging blog post about {topic}."},
                ],
                temperature=0.8,
                max_tokens=800
            )
            blog = response.choices[0].message.content
            st.success("✅ Blog Generated!")
            st.write(blog)

            # Option to download
            st.download_button("Download Blog", blog, file_name="blog.txt")
