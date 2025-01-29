from fastapi.testclient import TestClient
from patient_triage import rag_main  

client = TestClient(rag_main)

def test_assign_triage_level():
    response = client.post(
        "/assign-triage-level/",
        data={
            "symptoms": "Severe chest pain, radiating to the left arm, sweating, nausea.",
            "history": "High blood pressure, family history of heart disease.",
            "diagnosis": "Suspected myocardial infarction."
        }
    )
    assert response.status_code == 200
    result = response.json()
    assert result["final_output"]["triage_level"] == "Level 1 (Resuscitation)"
    assert "myocardial infarction" in result["final_output"]["explanation"]

def test_retrieve_context_from_chromadb():
    query = "Severe chest pain, radiating to the left arm, sweating, nausea."
    documents, metadatas, distances = rag_main.retrieve_context_from_chromadb(query)
    assert len(documents) > 0
    assert "myocardial infarction" in documents[0].lower()