from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)
completion = client.chat.completions.create(
    model="llama-3.2-90b-vision-preview",
    messages=[
        {
            "role": "user",
            "content": "Patient Medical Report\n\nSymptoms: Severe chest pain, radiating to the left arm, sweating, nausea.\nHistory: High blood pressure, family history of heart disease.\nPreliminary Diagnosis: Suspected myocardial infarction (heart attack).\n\ngive the patient triage level for this patient. \nThe application will assign one of 5 triage levels:\nLevel 1: Resuscitation (Immediate life-threatening condition).\nLevel 2: Emergency (Potentially life-threatening condition).\nLevel 3: Urgent (Serious but not life-threatening condition).\nLevel 4: Semi-Urgent (Less serious condition).\nLevel 5: Non-Urgent (Minor or stable condition).\n"
        },
        {
            "role": "assistant",
            "content": "Based on the symptoms and preliminary diagnosis, I would assign a triage level of:\n\n**Level 2: Emergency (Potentially life-threatening condition)**\n\nThe patient is experiencing severe chest pain, radiating to the left arm, sweating, and nausea, which are classic symptoms of a heart attack. The patient's history of high blood pressure and family history of heart disease also increase the risk of a life-threatening condition. While the condition is not immediately life-threatening (Level 1), it is potentially life-threatening and requires prompt medical attention, making it a Level 2: Emergency."
        },
        {
            "role": "user",
            "content": "Patient Medical Report\n\nSymptoms: Severe chest pain, radiating to the left arm, sweating, nausea.\nHistory: High blood pressure, family history of heart disease.\nPreliminary Diagnosis: Suspected myocardial infarction (heart attack).\n\ngive the patient triage level for this patient. \nThe application will assign one of 5 triage levels:\nLevel 1: Resuscitation (Immediate life-threatening condition).\nLevel 2: Emergency (Potentially life-threatening condition).\nLevel 3: Urgent (Serious but not life-threatening condition).\nLevel 4: Semi-Urgent (Less serious condition).\nLevel 5: Non-Urgent (Minor or stable condition).\n\n"
        },
        {
            "role": "assistant",
            "content": "Based on the symptoms and preliminary diagnosis, I would assign a triage level of:\n\n**Level 1: Resuscitation (Immediate life-threatening condition)**\n\nThe patient is experiencing severe chest pain, radiating to the left arm, sweating, and nausea, which are classic symptoms of a heart attack. This condition is considered an immediate life-threatening emergency, as timely intervention is critical to prevent cardiac damage or death. The patient requires immediate medical attention and stabilization, making it a Level 1: Resuscitation."
        },
        {
            "role": "user",
            "content": "Symptoms: Severe difficulty breathing, blue lips, unresponsive.\nHistory: Asthma, recent respiratory infection.\nPreliminary Diagnosis: Suspected severe asthma attack or respiratory arrest.\n\ngive the triage level 1-5\nTriage Level"
        },
        {
            "role": "assistant",
            "content": "Based on the symptoms and preliminary diagnosis, I would assign a triage level of:\n\n**Level 1: Resuscitation (Immediate life-threatening condition)**\n\nThe patient is experiencing severe difficulty breathing, blue lips (cyanosis), and unresponsive, which are signs of a severe and potentially life-threatening respiratory distress. This condition is an immediate life-threatening emergency, as the patient may not be getting enough oxygen to the brain and other vital organs, which can lead to brain damage or death within minutes. The patient requires immediate medical attention, including possible cardiopulmonary resuscitation and oxygen therapy, making it a Level 1: Resuscitation."
        },
        {
            "role": "user",
            "content": "Symptoms: Persistent chest pain, radiating to jaw, shortness of breath, nausea.\nHistory: Diabetes, high cholesterol.\nPreliminary Diagnosis: Suspected myocardial infarction (heart attack).\n\ngive the triage level 1-5\nTriage Level\n"
        },
        {
            "role": "assistant",
            "content": "Based on the symptoms and preliminary diagnosis, I would assign a triage level of:\n\n**Level 1: Resuscitation (Immediate life-threatening condition)**\n\nThe patient is experiencing persistent chest pain, radiating to the jaw, shortness of breath, and nausea, which are classic symptoms of a heart attack. This condition is an immediate life-threatening emergency, as the patient may be experiencing a potentially fatal blockage of a coronary artery. The patient's history of diabetes and high cholesterol also increases the risk of a life-threatening cardiac event. The patient requires immediate medical attention and stabilization, making it a Level 1: Resuscitation."
        },
        {
            "role": "user",
            "content": "Symptoms: High fever (39.5°C/103°F), rash on the torso, neck stiffness.\nHistory: Recent travel to a region with meningitis outbreak.\nPreliminary Diagnosis: Suspected meningitis.\n\ngive the triage level 1-5\nTriage Level\n"
        },
        {
            "role": "assistant",
            "content": "Based on the symptoms and preliminary diagnosis, I would assign a triage level of:\n\n**Level 1: Resuscitation (Immediate life-threatening condition)**\n\nThe patient is experiencing high fever, rash on the torso, and neck stiffness, which are classic symptoms of meningitis, a potentially life-threatening infection. The patient's recent travel to a region with a meningitis outbreak increases the likelihood of this diagnosis. Meningitis can cause severe complications, such as brain damage, and can progress rapidly, making timely treatment essential. The patient requires immediate medical attention, including stabilization and possible antibiotic treatment, making it a Level 1: Resuscitation."
        },
        {
            "role": "user",
            "content": "Symptoms: High fever (39.5°C/103°F), rash on the torso, neck stiffness.\nHistory: Recent travel to a region with meningitis outbreak.\nPreliminary Diagnosis: Suspected meningitis.\n\ngive the triage level 1-5\nTriage Level"
        },
        {
            "role": "assistant",
            "content": "Based on the symptoms and preliminary diagnosis, I would assign a triage level of:\n\n**Level 1: Resuscitation (Immediate life-threatening condition)**\n\nMeningitis is a medical emergency that requires immediate attention. The patient's symptoms, including high fever, rash, and neck stiffness, are consistent with a potentially life-threatening infection. The recent travel history to a region with a meningitis outbreak further increases the risk. Immediate treatment is crucial to prevent serious complications, such as brain damage or death. Therefore, the patient requires immediate medical attention, making it a Level 1: Resuscitation."
        },
        {
            "role": "user",
            "content": "Symptoms: Mild abdominal pain, no fever, no vomiting, able to eat.\nHistory: Occasional heartburn.\nPreliminary Diagnosis: Suspected gastritis.\n\ngive the triage level 1-5"
        },
        {
            "role": "assistant",
            "content": "Based on the symptoms and preliminary diagnosis, I would assign a triage level of:\n\n**Level 5: Non-Urgent (Minor or stable condition)**\n\nThe patient is experiencing mild abdominal pain, but is able to eat and does not have a fever or vomiting. The symptoms are consistent with a non-emergent condition such as gastritis, which can be managed with outpatient treatment. The patient's ability to eat and lack of severe symptoms suggest that the condition is not immediately life-threatening, making it a Level 5: Non-Urgent."
        },
        {
            "role": "user",
            "content": "Symptoms: Minor cut on the hand, no bleeding, no signs of infection.\nHistory: None significant.\nPreliminary Diagnosis: Superficial skin wound.\n\ngive the triage level 1-5"
        },
        {
            "role": "assistant",
            "content": "Based on the symptoms and preliminary diagnosis, I would assign a triage level of:\n\n**Level 5: Non-Urgent (Minor or stable condition)**\n\nThe patient has a minor cut on the hand with no bleeding and no signs of infection. The wound is superficial and does not require immediate medical attention. The patient is stable and can likely be treated with basic first aid, making it a Level 5: Non-Urgent."
        },
        {
            "role": "user",
            "content": "Symptoms: Severe headache, sudden onset, difficulty speaking, weakness on one side of the body.\nHistory: Hypertension, smoking.\nPreliminary Diagnosis: Suspected stroke.\n\ngive the triage level 1-5"
        },
        {
            "role": "assistant",
            "content": "Based on the symptoms and preliminary diagnosis, I would assign a triage level of:\n\n**Level 1: Resuscitation (Immediate life-threatening condition)**\n\nThe patient is experiencing severe symptoms, including sudden onset of headache, difficulty speaking, and weakness on one side of the body, which are classic signs of a stroke. Stroke is a medical emergency that requires immediate attention, as timely treatment can significantly impact outcomes and prevent long-term damage. The patient's history of hypertension and smoking also increases the risk of stroke. The patient requires immediate medical attention, including possible thrombolytic therapy, making it a Level 1: Resuscitation."
        },
        {
            "role": "user",
            "content": "Symptoms: Sore throat, mild fever, swollen lymph nodes, able to eat and drink.\nHistory: Seasonal allergies.\nPreliminary Diagnosis: Suspected viral pharyngitis.\ngive the triage level 1-5\n"
        },
        {
            "role": "assistant",
            "content": "Based on the symptoms and preliminary diagnosis, I would assign a triage level of:\n\n**Level 5: Non-Urgent (Minor or stable condition)**\n\nThe patient is experiencing a sore throat, mild fever, and swollen lymph nodes, which are consistent with a viral pharyngitis (a common cold or viral infection). The patient is able to eat and drink, which suggests that the condition is not severe. The patient's history of seasonal allergies may also be contributing to the symptoms, but does not indicate a more serious condition. The symptoms can likely be managed with self-care and over-the-counter medications, making it a Level 5: Non-Urgent."
        },
        {
            "role": "user",
            "content": "Symptoms: Sudden onset of severe abdominal pain, vomiting, inability to pass stool.\nHistory: Previous abdominal surgery.\nPreliminary Diagnosis: Suspected bowel obstruction.\n\ngive the triage level 1-5"
        },
        {
            "role": "assistant",
            "content": "Based on the symptoms and preliminary diagnosis, I would assign a triage level of:\n\n**Level 2: Emergency (Potentially life-threatening condition)**\n\nThe patient is experiencing sudden onset of severe abdominal pain, vomiting, and inability to pass stool, which are consistent with a bowel obstruction. This is a potentially life-threatening condition that requires prompt medical attention. The patient's history of previous abdominal surgery increases the risk of bowel obstruction. If left untreated, bowel obstruction can lead to serious complications, such as tissue death, perforation, and peritonitis. The patient requires immediate evaluation and possible surgical intervention, making it a Level 2: Emergency."
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print(completion.choices[0].message)
