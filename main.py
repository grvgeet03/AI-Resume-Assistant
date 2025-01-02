from dotenv import load_dotenv
import streamlit as st
import os
import io
import base64
import PyPDF2
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Streamlit page configuration
st.set_page_config(page_title='AI Resume Assistant')

# Configure the Gemini API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key for Google Generative AI is missing.")
else:
    genai.configure(api_key=api_key)

# Function to get Gemini response
def get_gemini_response(input_text, pdf_content, prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([input_text, pdf_content, prompt])
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

# Function to extract text from uploaded PDF using PyPDF2
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            # Read PDF content
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            # Return extracted text from the PDF
            return text
        except Exception as e:
            st.error(f"Error processing PDF: {e}")
            return None
    else:
        raise FileNotFoundError("No File Uploaded")

# Streamlit Application UI
st.header('ATS Assistant')
input_text = st.text_area('Job Description', key='input')
uploaded_file = st.file_uploader("Upload your Resume (PDF)...", type=['pdf'])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

# Buttons for user actions
submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")

# Input prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of technical roles like Data Science, Software Engineering, Full Stack Development, Data Engineering, etc., and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First, the output should come as a percentage, then keywords missing, and last, final thoughts.
"""

# Action: "Tell Me About the Resume"
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content:
            response = get_gemini_response(input_text, pdf_content, input_prompt1)
            if response:
                st.subheader("The Response is")
                st.write(response)
    else:
        st.write("Please upload the resume.")

# Action: "Percentage Match"
if submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content:
            response = get_gemini_response(input_text, pdf_content, input_prompt2)
            if response:
                st.subheader("The Response is")
                st.write(response)
    else:
        st.write("Please upload the resume.")
