# Grant AI Test App

A minimal Streamlit application integrated with OpenAI API for testing cloud deployment and secure environment variable configuration.

---

## 🚀 Features

- Streamlit web interface
- OpenAI API integration
- Secure environment variable handling
- Ready for Streamlit Cloud deployment

---

## 📦 Requirements

Dependencies are listed in `requirements.txt`.

---

## ▶️ Run Locally

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py

---

## 🔐 Environment Variable

Set your OpenAI API key before running:

Windows (PowerShell):

setx OPENAI_API_KEY "your_api_key_here"

Restart terminal after setting the key.

---

## ☁️ Deployment

Deploy using Streamlit Community Cloud:

1. Push code to GitHub
2. Create new app on https://share.streamlit.io
3. Add OPENAI_API_KEY in App Settings → Secrets

---

Built for structured AI deployment practice.
