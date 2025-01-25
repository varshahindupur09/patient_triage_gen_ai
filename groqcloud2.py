from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = "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"

# if not api_key:
#     print("Error: GROQ_API_KEY not found in the environment variables. Please check your .env file.")
#     exit()

# Initialize the Groq client
client = Groq(api_key=api_key)

# Define the messages for the chat completion
messages = [
    {
        "role": "user",
        "content": (
            "Patient Medical Report\n\n"
            "Symptoms: Severe chest pain, radiating to the left arm, sweating, nausea.\n"
            "History: High blood pressure, family history of heart disease.\n"
            "Preliminary Diagnosis: Suspected myocardial infarction (heart attack).\n\n"
            "Give the patient triage level for this patient. \n"
            "The application will assign one of 5 triage levels:\n"
            "Level 1: Resuscitation (Immediate life-threatening condition).\n"
            "Level 2: Emergency (Potentially life-threatening condition).\n"
            "Level 3: Urgent (Serious but not life-threatening condition).\n"
            "Level 4: Semi-Urgent (Less serious condition).\n"
            "Level 5: Non-Urgent (Minor or stable condition).\n"
        ),
    },
    {
        "role": "assistant",
        "content": (
            "Based on the symptoms and preliminary diagnosis, I would assign a triage level of:\n\n"
            "**Level 1: Resuscitation (Immediate life-threatening condition)**\n\n"
            "The patient is experiencing severe chest pain, radiating to the left arm, sweating, "
            "and nausea, which are classic symptoms of a heart attack. This condition is "
            "considered an immediate life-threatening emergency, as timely intervention is critical "
            "to prevent cardiac damage or death. The patient requires immediate medical attention and stabilization, "
            "making it a Level 1: Resuscitation."
        ),
    }
]

# Try to get the response from the Groq API
try:
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
    )

    # Print the assistant's response
    print(completion.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
