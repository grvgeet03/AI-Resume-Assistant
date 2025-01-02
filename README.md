# AI Resume Assistant

AI Resume Assistant is a Generative AI-powered career coaching application built with Streamlit. This tool allows users to upload their resumes as PDF files, compare them against job descriptions, and get compatibility scores along with professional insights.

## Features
- Upload your resume in PDF format.
- Compare your resume with a job description.
- Get a compatibility score and detailed feedback on your strengths, weaknesses, and missing keywords.
- Powered by Google Gemini API for advanced AI analysis.

## Technology Stack
- **Python**: Core language for application development.
- **Streamlit**: Framework for building an interactive web application.
- **PyODF2**: Library for processing and extracting text from PDF files.
- **Google Gemini API**: For Generative AI capabilities.
- **dotenv**: For securely managing environment variables.


## Installation Steps
1. **Clone the Repository**  
   Download the repository to your local machine using Git or as a ZIP file from GitHub.

2. **Set Up a Virtual Environment**  
   Create and activate a virtual environment to manage dependencies for the project.

3. **Install Dependencies**  
   Use the `requirements.txt` file to install all the required Python libraries.

4. **Set Up Environment Variables**  
   - Create a `.env` file in the project directory.  
   - Add your **Google Gemini API Key** to the `.env` file with the variable name `GOOGLE_API_KEY`.

5. **Run the Application**  
   Start the Streamlit app to access the ATS Resume Assistant.

6. **Access the Web App**  
   Open the URL displayed in the terminal (usually `http://localhost:8501`) in your web browser to use the app.

## Environment Variables
Create a `.env` file in the project directory and add the following line:

GOOGLE_API_KEY=your_google_gemini_api_key


## Usage
1. Launch the application.
2. Paste the job description into the text area.
3. Upload your resume in PDF format.
4. Click on the provided buttons to receive insights and compatibility scores.

## Contributing
Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request.


---

**Note:** Ensure your `.env` file is included in `.gitignore` to prevent exposing sensitive API keys.
