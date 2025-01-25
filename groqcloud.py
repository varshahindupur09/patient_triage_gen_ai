from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
# api_key = os.getenv("GROQ_API_KEY")
api_key = "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"
client = Groq(api_key=api_key)
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
    {
        "role": "user",
        "content": "Patient Medical Report\n\nSymptoms: Severe chest pain, radiating to the left arm, sweating, nausea.\nHistory: High blood pressure, family history of heart disease.\nPreliminary Diagnosis: Suspected myocardial infarction (heart attack).\n\ngive the patient triage level for this patient."
    },
    {
        "role": "assistant",
        "content": "Based on the symptoms and preliminary diagnosis, I would assign a triage level of:\n\n**Level 1: Resuscitation (Immediate life-threatening condition)**..."
    },
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

# print(completion.choices[0].message)
print(completion.choices[0].message.content)