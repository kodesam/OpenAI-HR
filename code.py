import streamlit as st
import openai

def compare_job_description_resume(file_job_description, file_resume):
    openai.api_key = ''  # Replace with your OpenAI API key
    
    # Decode bytes into string assuming UTF-8 encoding
    job_description = file_job_description.read().decode("utf-8")
    resume = file_resume.read().decode("utf-8")
    
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "You are a hiring manager."},
          {"role": "user", "content": job_description},
          {"role": "user", "content": resume},
      ]
    )
    
    similarity_score = response.choices[-1].message.content
    
    return similarity_score

# Streamlit app
st.title("Job Description and Resume Comparison")
file_job_description = st.file_uploader("Upload Job Description")
file_resume = st.file_uploader("Upload Resume")

if file_job_description is not None and file_resume is not None:
    score = compare_job_description_resume(file_job_description, file_resume)
    st.write("Similarity Score:", score)