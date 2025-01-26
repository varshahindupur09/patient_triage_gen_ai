from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("GROQ_API_KEY")

# Initialize the Groq client
client = Groq(api_key=api_key)

# Function to collect patient medical report input
def get_patient_report():
    symptoms = input("Enter symptoms: ")
    history = input("Enter patient history: ")
    diagnosis = input("Enter preliminary diagnosis: ")
    
    return (
        f"Patient Medical Report\n\n"
        f"Symptoms: {symptoms}\n"
        f"History: {history}\n"
        f"Preliminary Diagnosis: {diagnosis}\n\n"
        f"Give the patient triage level for this patient. \n"
        f"The application will assign one of 5 triage levels:\n"
        f"Level 1: Resuscitation (Immediate life-threatening condition).\n"
        f"Level 2: Emergency (Potentially life-threatening condition).\n"
        f"Level 3: Urgent (Serious but not life-threatening condition).\n"
        f"Level 4: Semi-Urgent (Less serious condition).\n"
        f"Level 5: Non-Urgent (Minor or stable condition).\n"
    )

# Get the patient's medical report
user_input = get_patient_report()

# Define the messages for the chat completion
messages = [
    {
        "role": "user",
        "content": user_input,
    }
]

# Try to get the response from the Groq API
try:
    completion = client.chat.completions.create(
        # model="llama-3.3-70b-versatile",
        model = "llama-3.2-90b-vision-preview",
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
