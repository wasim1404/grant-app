import streamlit as st
import os
from openai import OpenAI

st.title("Grant AI Test App")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("OPENAI_API_KEY is not set.")
else:
    client = OpenAI(api_key=OPENAI_API_KEY)

    if st.button("Test OpenAI"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Say hello professionally."}]
        )
        st.write(response.choices[0].message.content)
