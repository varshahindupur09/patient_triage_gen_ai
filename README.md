# patient_triage
Designed and implemented a console-based Patient Triage RAG Application to analyze medical reports and assign triage levels (1-5) based on condition severity. Leveraged a knowledge base of medical guidelines and an open-source medical model served via Ollama to retrieve insights and generate detailed, real-time explanations for triage decisions.


GroqCloud API: <your-groqcloud-api-key>


uvicorn main:app --reload --host 0.0.0.0 --port 8000
