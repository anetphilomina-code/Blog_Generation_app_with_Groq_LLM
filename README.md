# 📝 Blog Generator App using Groq LLM

This is an AI-powered **Blog Generation App** built with **Streamlit** and the **Groq API** (using Llama model).  
It allows users to instantly generate creative, structured blog articles based on custom topics or keywords.
---

## 🚀 Features

-  Generate unique blog posts instantly  
-  Powered by **Groq’s Llama LLM** for fast inference  
-  Context-aware and creative text generation  
-  Easy-to-use **Streamlit interface**  
-  Secure API key management using `.env` file  
  
---

##  Requirements

- **Python 3.10+**
- **Streamlit** – for the web interface  
- **Groq API (Llama model)** – for AI text generation  
- **dotenv** – for API key security  
- **VS Code** – for development
- Install dependencies:

  ` pip install -r requirements.txt`
  
- Create a .env file in the project root:

   `GROQ_API_KEY=your_api_key_here`
  
- Run the app:

   `streamlit run blog_app.py`
---
## Project Structure

```
Blog-Generator-App-using-Groq
│
├── blog_app.py      # Main Streamlit app file
├── requirements.txt # Python dependencies
├── .gitignore       # To ignore .env and other files
├── .env             # API key file (not uploaded)
└── README.md        # Project documentation
```


