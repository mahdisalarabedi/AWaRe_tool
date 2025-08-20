def AB_Prescribing(age, sex, chief_complaint, onset_symptoms, physcial_exam=None,  definitive_diagnosis=None, 
                    past_medical=None
                    ,Drug_allergy=None):    
    from openai import OpenAI
    from pydantic import BaseModel
    client = OpenAI()

    class Step(BaseModel):
        explanation: str
        output: str

    class Clinical_prescribing(BaseModel):
        steps: list[Step]
        final_answer: str
# handling variables
    past_medical= past_medical or "No known past medical"
    Drug_allergy= Drug_allergy or "No known drug allergy"
    physcial_exam=physcial_exam or "normal examination"
    print(past_medical, Drug_allergy, physcial_exam)
    if definitive_diagnosis==None:
        patient=f"""A {age} year old {sex} has come to me with a {chief_complaint} 
            since{onset_symptoms} days ago.
            physcial examination reveals {physcial_exam}
            the patient currently consumes{past_medical}
            the patient is allergic to{Drug_allergy}"""
        response = client.responses.parse(
            model="gpt-4o-2024-08-06",
            input=[
            {
                "role": "system",
                "content": """You are a primary-care doctor assistant. Guide the doctor with
                anti-biotic prescription if needed,
                provide all available choices and the best recommendation,
                if they were all equal
                tell.
                step by step.
                based on the file you are provided.""",
            },
            {   "role": "user", "content": patient
            },
            ],
    
            tools=[{
            "type": "file_search",
            "vector_store_ids": ["vs_68a2e40cdd6c8191b8eabb5906bda8e7"]
            }],
            text_format=Clinical_prescribing
            )

    else:
        patient=f"""A {age} year old {sex} has come to me, the diagnosis is{definitive_diagnosis}
                the patient history is {past_medical} and is allergic to {Drug_allergy}"""
        response = client.responses.parse(
            model="gpt-4o-2024-08-06",
            input=[
            {
                "role": "system",
                "content": """You are a primary-care doctor assistant. Guide the doctor with
                anti-biotic prescription if needed,
                provide all available choices and the best recommendation,
                if they were all equal
                tell.
                step by step.
                based on the file you are provided.""",
            },
            {   "role": "user", "content":patient
             },
            ],
    
            tools=[{
            "type": "file_search",
            "vector_store_ids": ["vs_68a2e40cdd6c8191b8eabb5906bda8e7"]
            }],
            text_format=Clinical_prescribing
            )

# If the model refuses to respond, you will get a refusal message

    Clinical_prescribing = response.output_parsed
    return(patient ,Clinical_prescribing.steps, Clinical_prescribing.final_answer)

#answer=AB_Prescribing(20, 'female', 'burning sensation in vagina', 5)
#print(answer[1])