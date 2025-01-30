# 🏥 **Patient Triage Gen AI**  
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-00BFFF?style=flat&logo=groq&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF4500?style=flat&logo=chromadb&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-000000?style=flat&logo=rag&logoColor=white)

**Patient Triage Gen AI** is an intelligent application designed to prioritize patients based on the severity of their medical conditions. It uses a **Retrieval-Augmented Generation (RAG)** architecture powered by **Groq** and **ChromaDB** to provide accurate and context-aware triage recommendations.  

---

## 🚀 **Key Features**
- **Patient Triage Levels**: Assigns one of 5 triage levels based on severity:
  - Level 1: Resuscitation (Immediate life-threatening condition)
  - Level 2: Emergency (Potentially life-threatening condition)
  - Level 3: Urgent (Serious but not life-threatening condition)
  - Level 4: Semi-Urgent (Less serious condition)
  - Level 5: Non-Urgent (Minor or stable condition)
- **Knowledge Base**: Uses a comprehensive database of medical guidelines and protocols for triage.
- **RAG Architecture**: Combines retrieval of relevant guidelines with generative AI for detailed explanations.
- **Console-Based Interface**: Provides a user-friendly console interface for input and output.
- **Real-Time Processing**: Generates triage reports in real-time using Groq's high-performance LLM.

---

## 🛠️ **Tech Stack**
- **Backend**: FastAPI
- **AI Model**: Groq (LLaMA 3.2-90B Vision Preview)
- **Vector Database**: ChromaDB
- **Embeddings**: Sentence Transformers (`all-MiniLM-L6-v2`)
- **Console Interface**: Rich (for formatted output)
- **Environment Management**: Python Virtual Environment (`.venv`)

---

## 📂 **Repository Structure**
