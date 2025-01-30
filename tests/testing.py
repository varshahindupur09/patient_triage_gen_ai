from fastapi.testclient import TestClient
from patient_triage.rag_main  import app
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def run_around_tests():
    # Setup: Clear and re-initialize ChromaDB before each test
    from patient_triage.rag_main import collection, add_guidelines_to_chromadb
    collection.delete()
    add_guidelines_to_chromadb()
    yield

@pytest.fixture(autouse=True)
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
    print(result)
    # assert result["final_output"]["triage_level"] == "Level 1 (Resuscitation)"
    # assert "myocardial infarction" in result["final_output"]["explanation"]

def test_retrieve_context_from_chromadb():
    query = "Severe chest pain, radiating to the left arm, sweating, nausea."
    documents, metadatas, distances = app.retrieve_context_from_chromadb(query)
    assert len(documents[0]) > 0
    # assert "myocardial infarction" in documents[0].lower()

run_around_tests()
test_assign_triage_level()
test_retrieve_context_from_chromadb()