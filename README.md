# 🎥 Agentic-AI Video Analysis

This project is a Flask-based web application that analyzes YouTube videos using LLMs (Large Language Models) and Google's YouTube Data API. It extracts metadata such as the title, channel information, publishing date, and description of the video and provides a summarized analysis.

## 🚀 Features
- Analyze YouTube videos by URL.
- Extracts and displays video metadata.
- Summarizes video content.
- Powered by CrewAI and Google's YouTube Data API.
- Frontend with simple Flask templates.

## 🛠️ Technologies Used
- Python
- Flask
- CrewAI
- Google API Client (YouTube Data API v3)
- Gemini LLM (Google)

## 📄 Project Structure
- `app.py` — Main Flask application with all routes and logic.
- `templates/index.html` — Frontend for submitting video URLs.
- `requirements.txt` — Python dependencies (you should create this if it doesn't exist yet).

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Agentic-AI-YouTube-Analysis.git
   cd Agentic-AI-YouTube-Analysis
   ```

2. **Install dependencies:**
   ```bash
   pip install flask google-api-python-client crewai
   ```

3. **Set environment variables:**
   - `GEMINI_API_KEY` — Your Gemini LLM API key.
   - `GOOGLE_API_KEY` — Your YouTube Data API key.

   These are already hardcoded for local testing but should be moved to a secure environment in production.

4. **Run the app:**
   ```bash
   python app.py
   ```

5. **Open your browser:**
   ```
   http://127.0.0.1:5000/
   ```

## 📬 API Endpoint

- `POST /analyze`
  - **Body:** `{ "url": "https://www.youtube.com/watch?v=example" }`
  - **Returns:** Video analysis as JSON.

## ⚠️ Important Notes
- Make sure the API keys you use have the necessary permissions.
- Hardcoding API keys is **not recommended** for production use. Use environment variables or a secure vault.
- Usage limits on the Google APIs apply.

## 📄 License
This project is open-source under the [MIT License](LICENSE).

---

Built with ❤️ for AI-driven insights into video content!
