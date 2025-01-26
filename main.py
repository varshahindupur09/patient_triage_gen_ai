from fastapi import FastAPI, HTTPException, Form
from groq import Groq
from chromadb import Client
import chromadb
from dotenv import load_dotenv
import os
import uvicorn

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Initialize ChromaDB
chromadb_client = Client()
collection = chromadb_client.create_collection("medical_guidelines")

# Define FastAPI app
app = FastAPI()

# Function to add documents to ChromaDB
def add_guidelines_to_chromadb():
    guidelines = [
        {
            "id": "1",
            "text": "Patients with severe chest pain and radiating pain to the left arm may be experiencing a myocardial infarction (heart attack). Assign Level 1 (Resuscitation).",
            "metadata": {"condition": "myocardial infarction", "level": 1},
        },
        {
            "id": "2",
            "text": "Patients experiencing severe difficulty breathing, blue lips, and unresponsiveness may be in respiratory arrest or have a severe asthma attack. Assign Level 1 (Resuscitation).",
            "metadata": {"condition": "severe asthma attack or respiratory arrest", "level": 1},
        },
        {
            "id": "3",
            "text": "Patients with persistent chest pain radiating to the jaw, shortness of breath, and nausea may be experiencing a myocardial infarction (heart attack). Assign Level 1 (Resuscitation).",
            "metadata": {"condition": "myocardial infarction", "level": 1},
        },
        {
            "id": "4",
            "text": "Patients with high fever, rash, neck stiffness, and recent travel to a meningitis outbreak region may have meningitis. Assign Level 1 (Resuscitation).",
            "metadata": {"condition": "meningitis", "level": 1},
        },
        {
            "id": "5",
            "text": "Patients with mild abdominal pain, no fever, no vomiting, and the ability to eat may have gastritis. Assign Level 5 (Non-Urgent).",
            "metadata": {"condition": "gastritis", "level": 5},
        },
        {
            "id": "6",   
            "text": "Patients with a minor cut on the hand, no bleeding, and no signs of infection may have a superficial skin wound. Assign Level 5 (Non-Urgent).",
            "metadata": {"condition": "superficial skin wound", "level": 5},
        },
        {
            "id": "7",
            "text": "Patients experiencing a sudden severe headache, difficulty speaking, and weakness on one side of the body may be having a stroke. Assign Level 1 (Resuscitation).",
            "metadata": {"condition": "stroke", "level": 1},
        },
        {
            "id": "8",
            "text": "Patients with a sore throat, mild fever, swollen lymph nodes, and the ability to eat and drink may have viral pharyngitis. Assign Level 5 (Non-Urgent).",
            "metadata": {"condition": "viral pharyngitis", "level": 5},
        },
        {
            "id": "9",
            "text": "Patients with sudden onset of severe abdominal pain, vomiting, and inability to pass stool, especially with a history of abdominal surgery, may have a bowel obstruction. Assign Level 2 (Emergency).",
            "metadata": {"condition": "bowel obstruction", "level": 2},
        },  
    ]
    for guideline in guidelines:
        collection.add(
            documents=[guideline["text"]],
            metadatas=[guideline["metadata"]],
            ids=[guideline["id"]]
        )

# Call this once to initialize the database
add_guidelines_to_chromadb()

# Function to retrieve context from ChromaDB
def retrieve_context_from_chromadb(query):
    results = collection.query(query_texts=[query], n_results=3)
    combined_context = " ".join([res["text"] for res in results["documents"]])
    return combined_context

# Function to generate triage report
def generate_triage_report_with_rag(symptoms, history, diagnosis):
    # Create user input
    user_input = (
        f"Patient Medical Report\n\n"
        f"Symptoms: {symptoms}\n"
        f"History: {history}\n"
        f"Preliminary Diagnosis: {diagnosis}\n\n"
    )

    # Retrieve relevant context
    query = f"Symptoms: {symptoms}, History: {history}, Diagnosis: {diagnosis}"
    retrieved_context = retrieve_context_from_chromadb(query)

    # Combine user input with retrieved context
    full_context = f"{retrieved_context}\n\n{user_input}"
    messages = [{"role": "user", "content": full_context}]

    # Query Groq API
    try:
        response = client.chat.completions.create(
            model="llama-3.2-90b-vision-preview",
            messages=messages,
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
        )
        return response.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error from Groq: {str(e)}")
    
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Patient Triage Application"}

@app.post("/assign-triage-level/")
async def assign_triage_level(
    symptoms: str = Form(...),
    history: str = Form(...),
    diagnosis: str = Form(...)
):
    try:
        result = generate_triage_report_with_rag(symptoms, history, diagnosis)
        return {"triage_result": result}
    except HTTPException as e:
        raise e

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # commited