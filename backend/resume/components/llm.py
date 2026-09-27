from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from .helperfunc import timer
from dotenv import load_dotenv
import os

load_dotenv()


@timer
def generation(job_description, retrieved_chunks):
    
    llm = ChatGoogleGenerativeAI(
        model = 'gemini-3.5-flash',
        api_key = os.getenv("GOOGLE_API_KEY"),
        temperature = 0.1
    )
    
    content = "\n\n".join(retrieved_chunks)
    
    prompt = f"""
    You are an expert technical recruiter and resume reviewer.

    Analyze the candidate's resume against the given job description.

    JOB DESCRIPTION:
    {job_description}

    RELEVANT RESUME CONTEXT:
    {content}

    Identify:

    1. Matching skills
    2. Missing skills
    3. Relevant experience
    4. Areas of improvement
    5. Specific suggestions to improve the resume for this job

    Important:
    - Only use information present in the resume context.
    - Do not invent candidate experience.
    - Clearly distinguish between skills that are present and skills that are missing.
    - Give concise and actionable suggestions.
    - use only the necessary symbols when it is needed, don't include the unwanted symbols like(#,*).
        """
    parser = StrOutputParser()
    chain = llm | parser 
    response = chain.invoke(prompt)
    return response
        
    
    