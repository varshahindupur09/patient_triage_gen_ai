# patient_triage
Designed and implemented a console-based Patient Triage RAG Application to analyze medical reports and assign triage levels (1-5) based on condition severity. Leveraged a knowledge base of medical guidelines and an open-source medical model served via Ollama to retrieve insights and generate detailed, real-time explanations for triage decisions.


GroqCloud API: <your-groq-api-key>


graph LR
    A[Patient Input] --> B[Embedding Model]
    B --> C[ChromaDB Vector Search]
    C --> D[Top 3 Guidelines]
    D --> E[LLM Prompt]
    E --> F[Structured Triage Output]