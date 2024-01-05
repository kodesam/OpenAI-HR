import streamlit as st
import openai
import PyPDF2
import docx

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = [page.extract_text() for page in reader.pages]
    return ' '.join(text)

def extract_text_from_word(file_path):
    doc = docx.Document(file_path)
    paragraphs = [para.text for para in doc.paragraphs]
    return ' '.join(paragraphs)

def compare_job_description_resume(file_job_description, file_resume):
    openai.api_key = ''  # Replace with your OpenAI API key
    
    # Extract text from PDF and Word documents
    if file_job_description.name.endswith('.pdf'):
        job_description = extract_text_from_pdf(file_job_description)
    elif file_job_description.name.endswith('.docx'):
        job_description = extract_text_from_word(file_job_description)
    else:
        raise ValueError('Unsupported file format. Please upload a PDF or Word document for the job description.')
    
    if file_resume.name.endswith('.pdf'):
        resume = extract_text_from_pdf(file_resume)
    elif file_resume.name.endswith('.docx'):
        resume = extract_text_from_word(file_resume)
    else:
        raise ValueError('Unsupported file format. Please upload a PDF or Word document for the resume.')
    
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
file_job_description = st.file_uploader("Upload Job Description", type=['pdf', 'docx'])
file_resume = st.file_uploader("Upload Resume", type=['pdf', 'docx'])

if file_job_description is not None and file_resume is not None:
    score = compare_job_description_resume(file_job_description, file_resume)
    st.write("Similarity Score:", score)