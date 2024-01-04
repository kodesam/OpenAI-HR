import openai

def compare_job_description_resume(file_job_description, file_resume):
    openai.api_key = 'YOUR_API_KEY'  # Replace with your OpenAI API key
    
    with open(file_job_description, 'r') as f:
        job_description = f.read()
    
    with open(file_resume, 'r') as f:
        resume = f.read()
    
    documents = [job_description, resume]
    
    response = openai.Answer.create(
      search_model="davinci",
      model="davinci",
      documents=documents,
      question=job_description,
      examples_context="What is the similarity score between the job description and the resume?",
      max_responses=1,
      stop=None,
      log_level="info",
    )
    
    similarity_score = response['answers'][0]['score']
    
    return similarity_score

# Example usage
file_job_description = '/path/to/job_description.txt'
file_resume = '/path/to/resume.txt'

score = compare_job_description_resume(file_job_description, file_resume)
print("Similarity Score:", score)
