import streamlit as st 
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai

import time
from pathlib import Path
import tempfile

from dotenv import load_dotenv
load_dotenv()

import os

API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

# Page configuration
st.set_page_config(
    page_title="Video AI Summarizer",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Clean and Professional Design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Background */
    .stApp {
        background: linear-gradient(to bottom, #0f172a, #1e293b);
    }
    
    /* Remove default padding */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 800px;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Headers */
    h1 {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 2.5rem !important;
        text-align: center;
        margin-bottom: 0.5rem !important;
    }
    
    h2 {
        color: #e2e8f0 !important;
        font-weight: 500 !important;
        font-size: 1.1rem !important;
        text-align: center;
        margin-bottom: 2rem !important;
        opacity: 0.9;
    }
    
    h3 {
        color: #60a5fa !important;
        font-weight: 600 !important;
        font-size: 1.3rem !important;
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
    }
    
    /* File Uploader */
    [data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.05);
        border: 2px dashed rgba(96, 165, 250, 0.3);
        border-radius: 12px;
        padding: 2rem;
        transition: all 0.3s ease;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: rgba(96, 165, 250, 0.6);
        background: rgba(255, 255, 255, 0.08);
    }
    
    [data-testid="stFileUploader"] section {
        border: none !important;
        padding: 0 !important;
    }
    
    [data-testid="stFileUploader"] label {
        color: #e2e8f0 !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
    }
    
    /* Text Area */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.95) !important;
        border: 2px solid rgba(96, 165, 250, 0.3) !important;
        border-radius: 12px !important;
        color: #1e293b !important;
        font-size: 1rem !important;
        padding: 1rem !important;
        min-height: 140px !important;
        transition: all 0.3s ease;
    }
    
    .stTextArea textarea:focus {
        border-color: #60a5fa !important;
        box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.1) !important;
        outline: none !important;
    }
    
    .stTextArea textarea::placeholder {
        color: #64748b !important;
    }
    
    .stTextArea label {
        color: #e2e8f0 !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
    }
    
    /* Button */
    .stButton button {
        background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.75rem 2rem !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4) !important;
    }
    
    .stButton button:active {
        transform: translateY(0) !important;
    }
    
    /* Video Player */
    video {
        border-radius: 12px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        width: 100%;
        margin: 1.5rem 0;
    }
    
    /* Info/Warning/Error Messages */
    .stAlert {
        border-radius: 10px !important;
        border: none !important;
        padding: 1rem 1.25rem !important;
    }
    
    [data-testid="stInfo"] {
        background: rgba(59, 130, 246, 0.15) !important;
        color: #93c5fd !important;
    }
    
    [data-testid="stWarning"] {
        background: rgba(251, 191, 36, 0.15) !important;
        color: #fcd34d !important;
    }
    
    [data-testid="stSuccess"] {
        background: rgba(34, 197, 94, 0.15) !important;
        color: #86efac !important;
    }
    
    [data-testid="stError"] {
        background: rgba(239, 68, 68, 0.15) !important;
        color: #fca5a5 !important;
    }
    
    /* Progress Bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, #3b82f6, #60a5fa) !important;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #60a5fa !important;
    }
    
    /* Feature Cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(96, 165, 250, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .feature-card:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(96, 165, 250, 0.4);
        transform: translateY(-4px);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 0.75rem;
    }
    
    .feature-title {
        color: #60a5fa;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        color: #cbd5e1;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    
    /* Divider */
    hr {
        border: none;
        border-top: 1px solid rgba(96, 165, 250, 0.2);
        margin: 2rem 0;
    }
    
    /* Results Section */
    .results-section {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(96, 165, 250, 0.2);
        border-radius: 12px;
        padding: 2rem;
        margin-top: 2rem;
    }
    
    .results-section h3 {
        margin-top: 0 !important;
    }
    
    .results-section p, .results-section li {
        color: #e2e8f0 !important;
        line-height: 1.7;
    }
    
    /* Markdown Content */
    .element-container p {
        color: #cbd5e1;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🎬 Video AI Summarizer")
st.markdown("##### ✨ Powered by Gemini 2.5 Flash & Google Generative AI")

st.markdown("<br>", unsafe_allow_html=True)


@st.cache_resource
def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        model=Gemini(id="gemini-2.5-flash"),
        tools=[DuckDuckGo()],
        markdown=True,
    )

# Initialize the agent
multimodal_Agent = initialize_agent()

# Features Section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎥</div>
        <div class="feature-title">Video Analysis</div>
        <div class="feature-desc">Advanced AI-powered video content analysis</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔍</div>
        <div class="feature-title">Smart Research</div>
        <div class="feature-desc">Automatic web research for deeper insights</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">AI Agent</div>
        <div class="feature-desc">Gemini-powered intelligent responses</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# File Upload Section
st.markdown("### 📤 Upload Your Video")
video_file = st.file_uploader(
    "Choose a video file (MP4, MOV, AVI)",
    type=['mp4', 'mov', 'avi'],
    help="Upload a video file for AI-powered analysis"
)

if video_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name

    st.success("✅ Video uploaded successfully!")
    
    # Video Preview
    st.markdown("### 🎬 Video Preview")
    st.video(video_path, format="video/mp4", start_time=0)

    # Question Input
    st.markdown("### 💭 Ask a Question About the Video")
    user_query = st.text_area(
        "What would you like to know?",
        placeholder="Examples:\n• Summarize the main points of this video\n• What are the key topics discussed?\n• Explain the concepts presented in detail\n• What insights can you provide about this content?",
        help="Ask any question about the video content. The AI will analyze it and provide detailed insights."
    )

    # Analyze Button
    if st.button("🔍 Analyze Video", type="primary", use_container_width=True):
        if not user_query:
            st.warning("⚠️ Please enter a question to analyze the video.")
        else:
            try:
                with st.spinner("🤖 Analyzing video... This may take a moment."):
                    # Upload and process video file
                    processed_video = upload_file(video_path)
                    
                    # Progress tracking
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    status_text.text("⏳ Uploading video to AI...")
                    progress_bar.progress(25)
                    
                    while processed_video.state.name == "PROCESSING":
                        time.sleep(1)
                        processed_video = get_file(processed_video.name)
                        status_text.text("🔄 Processing video content...")
                        progress_bar.progress(50)

                    status_text.text("🧠 Analyzing and researching...")
                    progress_bar.progress(75)

                    # Analysis prompt
                    analysis_prompt = f"""
                    Analyze the uploaded video for content and context.
                    Respond to the following query using video insights and supplementary web research:
                    {user_query}

                    Provide a detailed, user-friendly, and actionable response.
                    """

                    # AI agent processing
                    response = multimodal_Agent.run(analysis_prompt, videos=[processed_video])
                    
                    progress_bar.progress(100)
                    status_text.text("✅ Analysis complete!")
                    time.sleep(0.5)
                    progress_bar.empty()
                    status_text.empty()

                # Display results
                st.markdown('<div class="results-section">', unsafe_allow_html=True)
                st.markdown("### 📊 Analysis Results")
                st.markdown(response.content)
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.success("✨ Analysis completed successfully!")

            except Exception as error:
                st.error(f"❌ Error: {error}")
            finally:
                # Clean up
                Path(video_path).unlink(missing_ok=True)
    
else:
    st.info("👆 Please upload a video file to get started")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: rgba(226, 232, 240, 0.6); font-size: 0.9rem;">
    Made with ❤️ using Streamlit • Gemini AI • DuckDuckGo
</div>
""", unsafe_allow_html=True)

