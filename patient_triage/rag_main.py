from fastapi import FastAPI, HTTPException, Form, Request
from groq import Groq
from chromadb import Client, Documents, Embeddings
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import chromadb
from dotenv import load_dotenv
import os
import uvicorn
from pydantic import BaseModel
from typing import Dict, List, Union
import json
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Initialize ChromaDB
# add embeddings
embed_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
chromadb_client = Client()
collection = chromadb_client.create_collection(
    name="medical_guidelines",
    embedding_function=embed_fn
    )

# Define FastAPI app and response models
app = FastAPI()

# ===== CORS Middleware =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== Initialized rate limiter =====
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

class TriageStep(BaseModel):
    description: str
    # details: Dict[str, str] | List[str] | str
    # details: dict | list | str  # 3.10 version
    details: Union[dict, list, str]  # 3.9 version
    references: List[str] = []

class TriageResponse(BaseModel):
    steps: List[TriageStep]
    final_output: Dict[str, str]
    # final_output: dict  # 
    confidence: float
    guidelines_used: List[str]

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
    try:
        results = collection.query(
            query_texts=[query],
            n_results=3,
            include=["documents", "metadatas", "distances"]
        )
        return results["documents"], results["metadatas"], results["distances"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Retrieval error: {str(e)}")


# Modified function to generate structured triage report
def generate_structured_triage_report(symptoms: str, history: str, diagnosis: str) -> dict:
    # Retrieve relevant context
    query = f"Symptoms: {symptoms}, History: {history}, Diagnosis: {diagnosis}"
    documents, metadatas, distances = retrieve_context_from_chromadb(query)

    # Create structured prompt
    system_prompt = """You are a medical triage expert. Analyze the patient report and generate a structured response following these steps:

    1. Analyze Symptoms/History/Diagnosis
    2. Retrieve Relevant Guidelines
    3. Assign Triage Level
    4. Generate Explanation
    5. Final Output

    Follow this exact JSON format:
    {
        "steps": [
            {
                "description": "Analyzing Patient Report...",
                "details": {
                    "symptoms": ["list", "of", "key", "symptoms"],
                    "history": ["list", "of", "relevant", "history"],
                    "diagnosis": "preliminary diagnosis"
                }
            },
            {
                "description": "Retrieving Relevant Triage Guidelines...",
                "details": ["list", "of", "matched", "conditions"]
            },
            {
                "description": "Assigning Triage Level...",
                "details": {
                    "condition": "identified condition",
                    "level": "triage level with number"
                }
            },
            {
                "description": "Generating Explanation...",
                "details": "concise explanation linking symptoms/history to triage level"
            }
        ],
        "final_output": {
            "triage_level": "Level X (Category)",
            "explanation": "final concise explanation"
        }
    }"""

    user_input = f"""PATIENT DATA:
    - Symptoms: {symptoms}
    - History: {history}
    - Preliminary Diagnosis: {diagnosis}

    RELEVANT GUIDELINES:
    {documents}"""

    try:
        response = client.chat.completions.create(
            model="llama-3.2-90b-vision-preview",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.3,
            max_tokens=1024,
            top_p=1,
            response_format={"type": "json_object"}
        )

        response_data = json.loads(response.choices[0].message.content)

        # Calculate confidence score
        if distances:
            average_distance = sum(distances) / len(distances)
            confidence_score = 1 - average_distance  # Assuming distances are normalized between 0 and 1
        else:
            confidence_score = 0  # Default to 0 if no distances are available

        # Add RAG metadata
        response_data["confidence"] = confidence_score
        response_data["guidelines_used"] = [m["condition"] for m in metadatas]

        return response_data

    except json.JSONDecodeError:
        raise HTTPException(500, "Invalid JSON response from LLM")
    except Exception as e:
        raise HTTPException(500, f"Generation error: {str(e)}")


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Patient Triage Application"}

@app.post("/assign-triage-level/", response_model=TriageResponse)
@limiter.limit("10/minute")
async def assign_triage_level(
    request: Request,
    symptoms: str = Form(...),
    history: str = Form(...),
    diagnosis: str = Form(...)
):
    try:
        report = generate_structured_triage_report(symptoms, history, diagnosis)
        return report
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    add_guidelines_to_chromadb()
    uvicorn.run(app, host="0.0.0.0", port=8001)