import streamlit as st
from AB_Prescribing import AB_Prescribing
st.markdown(
    """
    <div style='direction: rtl; text-align: right; font-size:18px;'>
    لطفا پارامترهای زیر را تنظیم کنید</div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style='direction: rtl; text-align: right; font-size:18px;'>
    Age </div>
    """,
    unsafe_allow_html=True
)
st.session_state.age=st.number_input(label="Patient's age", min_value=0.1)

st.markdown(
    """
    <div style='direction: rtl; text-align: right; font-size:18px;'>
    Sex </div>
    """,
    unsafe_allow_html=True
)

st.session_state.sex=st.selectbox('Please select', ['female','male'])

st.session_state.chief_complaint=st.text_area('Feel in the chief complaint', value=None)


st.session_state.onset_symptoms=st.number_input(label="Days from symptoms's oset", min_value=1)

st.session_state.physical_exam=st.text_area('Physical exam findings, leave empty if everything is normal', value=None)

st.session_state.definitive_diagnosis=st.text_area('Definitve diagnosis if you guess something', value=None)

st.session_state.past_medical=st.text_area('Past medical history of patient, if any', value=None)

st.session_state.Drug_allergy=st.text_area('Drug allergy', value=None)

st.session_state.outcomes=()
if st.button(label="Let's perscribe 📄"):
    
    st.session_state.outcomes=AB_Prescribing(age=st.session_state.age, 
                                             sex=st.session_state.sex, 
                                             chief_complaint=st.session_state.chief_complaint,
                                             onset_symptoms=st.session_state.onset_symptoms,
                                             physcial_exam=st.session_state.physical_exam, 
                                             definitive_diagnosis=st.session_state.definitive_diagnosis,
                                             past_medical=st.session_state.past_medical,
                                             Drug_allergy=st.session_state.Drug_allergy)
    
    st.write(st.session_state.outcomes[2])
    
    st.write(st.session_state.outcomes[0])
    
    st.write(st.session_state.outcomes[1])
