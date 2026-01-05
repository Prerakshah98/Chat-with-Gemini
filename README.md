# Chat with Gemini - AI Assistant

## DESCRIPTION

This is a generative AI web application built using Python. It acts as a personal assistant that allows users to chat with Google's Gemini Flash model. The application features a simple web interface where users can input questions and receive real-time, intelligent responses.

I built this project to learn how to integrate Large Language Models (LLMs) into software applications without relying on paid APIs.

## FEATURES
- Real-time text generation using Google Gemini 2.0 Flash
- Simple, clean web interface
- Error handling for API connection issues
- Secure API key management

## TECH STACK
- Language: Python 3
- Framework: Streamlit (for the frontend web interface)
- AI Model: Google Gemini Flash (via Google GenAI SDK)
- Environment Management: Python-dotenv

## HOW TO RUN THIS PROJECT LOCALLY

1. Clone the repository or download the files.

2. Install the required libraries:
   pip install -r requirements.txt

3. Set up your API Key:
   - Create a file named .env in the same folder.
   - Add your Google API key inside it like this:
     GOOGLE_API_KEY=your_actual_api_key_here

4. Run the application:
   streamlit run app.py

5. The app will open automatically in your web browser.
