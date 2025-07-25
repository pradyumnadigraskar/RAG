# 🚀 RealTime RAG-based Chatbot

<p align="center">
  <img src="Banner.png" alt="Chatbot UI" width="400"/>
</p>

<p align="center">
  <b>Realtime, Document-Aware AI Chatbot with PDF Upload, Local LLM, and Summarization</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi"/>
  <img src="https://img.shields.io/badge/ChromaDB-VectorDB-orange?logo=chromadb"/>
  <img src="https://img.shields.io/badge/Mistral-7B-informational"/>
  <img src="https://img.shields.io/badge/Gemini-API-yellow"/>
</p>

---

# 📚 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Screenshots](#screenshots)
- [Setup & Installation](#setup--installation)
- [Usage Guide](#usage-guide)
- [Tech Stack](#tech-stack)
- [Main Dependencies](#main-dependencies)
- [Troubleshooting & FAQ](#troubleshooting--faq)
- [Security & Limitations](#security--limitations)
- [Contribution](#contribution)
- [Contact & Credits](#contact--credits)

---

# 📝 Overview

**RealTime RAG-based Chatbot** is a full-stack Retrieval-Augmented Generation (RAG) system that lets you chat with your own documents in real time! Upload PDFs, ask questions, and get context-aware answers using:
- **ChromaDB** for vector storage
- **Mistral 7B (GGUF)** for blazing-fast local LLM inference
- **Gemini API** for document summarization
- A custom, modern HTML/CSS frontend

---

# ✨ Features

- 📄 **PDF Upload & Ingestion**: Drag-and-drop PDFs for instant Q&A
- 🧠 **Semantic Search**: ChromaDB-powered persistent vector database
- 🤖 **Local LLM**: Mistral-7B-Instruct (.gguf) via llama.cpp/ctransformers
- ☁️ **Gemini API**: Summarizes PDFs before embedding
- 🌐 **FastAPI Backend**: Robust REST API
- 🎨 **Custom Frontend**: Responsive, modern UI
- 🔍 **Contextual Answers**: RAG pipeline ensures answers are grounded in your docs
- 🛡️ **Open Source & Extensible**: Easy to adapt for your own needs

---

# 🏗️ Architecture

```mermaid
graph TD;
  A[User Uploads PDF / Asks Question] --> B[Frontend (HTML/CSS)]
  B --> C[FastAPI Backend]
  C -->|PDF| D[Gemini API (Summarization)]
  D --> E[ChromaDB (Vector Store)]
  C -->|Query| E
  E --> F[Mistral 7B LLM (Local)]
  F --> G[Response to User]
```

---

# 🖼️ Screenshots

<p align="center">
  <img src="Main.png" alt="Chatbot UI" width="350"/>
  <img src="PDF.png" alt="PDF Upload" width="350"/>
  <img src="Query.png" alt="Custom Query" width="350"/>
</p>

> **Tip:** You can add your own PDFs and ask questions about them!

---

# ⚙️ Setup & Installation

## 1. Clone the Repository
```bash
git clone https://github.com/pradyumnadigraskar/RealTime_RagchatBot.git
cd RealTime_RagchatBot
```

## 2. Create & Activate Virtual Environment
```bash
python -m venv rag_env
rag_env\Scripts\activate   # Windows
# source rag_env/bin/activate   # Linux/Mac
```

## 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

## 4. Download Required Models
- **Mistral 7B .gguf**: Download from [HuggingFace](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) and place in a `models/` folder at the project root.
- **Check model path** in `backend/chain.py` matches your setup.

## 5. Set Up API Keys
- **Gemini API**: Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey) and set it as an environment variable:
  - On Windows:
    ```powershell
    $env:GOOGLE_API_KEY="your-key-here"
    ```
  - On Linux/Mac:
    ```bash
    export GOOGLE_API_KEY="your-key-here"
    ```
- (Optional) Use a `.env` file and `python-dotenv` for local development.

## 6. Ingest & Index PDF Manuals
```bash
python backend/ingest.py
```
*Embeddings are stored in persistent ChromaDB at `backend/chroma_db`.*

## 7. Run the FastAPI Backend
```bash
uvicorn backend.api:app --reload
```
Visit FastAPI docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## 8. Run the Frontend
- Open `enhanced_chat_app.html` in your browser
- Or serve it with a static server:
  ```bash
  python -m http.server 5500
  ```

---

# 🚦 Usage Guide

- **Upload PDFs**: Use the frontend to upload your own documents.
- **Ask Questions**: Type questions about the uploaded PDFs.
- **Get Answers**: The chatbot retrieves relevant chunks, runs them through the LLM, and responds.

## 💡 Sample Queries
- "What is the temperature description of Realme buds?"
- "What is low water alarm?"
- "How to reset a Dell Latitude laptop?"

---

# 🧰 Tech Stack

| Component         | Tool / Library                        |
|-------------------|---------------------------------------|
| Embeddings        | sentence-transformers (mpnet/MiniLM)  |
| Vector DB         | ChromaDB                              |
| LLM Inference     | ctransformers + Mistral 7B (.gguf)    |
| Summarization     | Google Gemini API                     |
| Backend API       | FastAPI                               |
| Frontend          | HTML + CSS                            |

---

# 📦 Main Dependencies

See `requirements.txt` for the full list. Key packages:
- fastapi
- uvicorn
- chromadb
- ctransformers
- sentence-transformers
- PyMuPDF
- requests
- openai
- python-dotenv

---

# 🛠️ Troubleshooting & FAQ

- ✅ **ChromaDB directory missing?** Ensure it exists before querying.
- ✅ **Model not found?** Verify the Mistral .gguf model path in `chain.py` and that the file is in `models/`.
- ✅ **Tokenizer/generator errors?** Check model path and compatibility.
- ✅ **UI freezes?** Check browser console for network errors.
- ✅ **API key issues?** Ensure `GOOGLE_API_KEY` is set in your environment.

---

# 🔒 Security & Limitations

- **No authentication**: All endpoints are public by default. Add auth for production use.
- **API keys in code**: Never commit real API keys. Use environment variables or `.env` files.
- **Model size**: Mistral 7B is resource-intensive; ensure your machine has enough RAM/CPU.
- **PDF parsing**: Complex PDFs may not be perfectly chunked or summarized.
- **No GPU support out-of-the-box**: For large-scale use, consider GPU acceleration.
- **Experimental**: This is a research/developer project, not production-ready.

---

# 🤝 Contribution

Contributions are welcome! To contribute:
1. Fork the repo
2. Create a new branch
3. Make your changes
4. Submit a pull request

For major changes, please open an issue first to discuss what you’d like to change.

---

# 📬 Contact & Credits

Made with ❤️ by Swaraj Solanke

- For issues or suggestions, open a GitHub issue or email: **pradyumnadigraskar11@gmail.com**
- GitHub: [https://github.com/pradyumnadigraskar](https://github.com/pradyumnadigraskar)

---

<p align="center">
  <b>Happy Chatting! 🚀</b>
</p>




