from flask import Flask, request, jsonify, render_template
import os
from crewai import Agent, Task, Crew, LLM
import googleapiclient.discovery
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

# Set up API keys
os.environ['GEMINI_API_KEY'] = "AIzaSyDSeRLOVOq_qTIVM0v6XSwBKEdYNkzZ7Og"
os.environ['GOOGLE_API_KEY'] = "AIzaSyCHegRg4QyqaImUR_U8ftJTdMomzxA7Fnc"
llm = LLM(model="gemini/gemini-1.5-flash", provider="gemini")

def get_youtube_video_info(url: str) -> str:
    try:
        youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=os.environ['GOOGLE_API_KEY'])
        if 'youtu.be' in url:
            video_id = url.split('/')[-1].split('?')[0]
        elif 'v=' in url:
            query = urlparse(url).query
            video_id = parse_qs(query)['v'][0]
        else:
            video_id = url.split('/')[-1]

        response = youtube.videos().list(part='snippet', id=video_id).execute()
        if not response['items']:
            return "No video found with the given URL"
        
        snippet = response['items'][0]['snippet']
        return f"""
📺 YouTube Video Analysis:
Title: {snippet['title']}
Channel: {snippet['channelTitle']}
Published: {snippet['publishedAt']}
Description:
{snippet['description']}
"""
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_video():
    try:
        data = request.get_json()
        video_url = data.get('url')

        researcher = Agent(
            role="YouTube Analyst",
            goal="Extract information from YouTube videos",
            backstory="Expert in analyzing video content",
            verbose=True,
            llm=llm
        )

        task = Task(
            description="Analyze the YouTube video at {video_url}",
            expected_output="Video title, channel info, and description and little summary about the video",
            agent=researcher,
            function=lambda video_url: get_youtube_video_info(video_url)
        )

        crew = Crew(
            agents=[researcher],
            tasks=[task],
            verbose=True
        )

        result = crew.kickoff(inputs={"video_url": video_url})

        return jsonify({ "result": str(result) })

    except Exception as e:
        # 👇 Always return JSON even on error
        return jsonify({ "error": str(e) }), 500

if __name__ == '__main__':
    app.run(debug=True)
