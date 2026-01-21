# 🎬 Video AI Summarizer

> 🚀 An advanced AI-powered video analysis tool using Gemini 2.5 Flash and Google Generative AI

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-4285F4?style=flat&logo=google&logoColor=white)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Video_Summarizer-black?style=flat&logo=github)](https://github.com/MustafaKocamann/Video-Summarizer-with-Phidata)

---

## 🌟 Features

| Feature | Description | Icon |
|---------|-------------|------|
| 🎥 **Video Analysis** | Advanced AI-powered video content analysis with frame-level understanding | Video Analysis |
| 🔍 **Smart Research** | Automatic web research using DuckDuckGo for deeper insights | Web Research |
| 🤖 **AI Agent** | Gemini-powered intelligent responses with context awareness | AI-Powered |
| 📊 **Detailed Reports** | Comprehensive analysis reports with structured information | Analytics |
| 🎨 **Professional UI** | Modern, clean, and user-friendly interface with dark theme | Design |
| ⚡ **Real-time Processing** | Fast video processing with progress tracking | Performance |

---

## 🚀 Quick Links

### 🌐 **Live Demo**
👉 **[Video AI Summarizer - Live App](https://video-summarizer-with-phidata.streamlit.app/)**

### 📖 **GitHub Repository**
👉 **[View on GitHub](https://github.com/MustafaKocamann/Video-Summarizer-with-Phidata)**

---

## 📋 Table of Contents

- [Features](#-features)
- [Quick Links](#-quick-links)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 💻 Installation

### 📌 Prerequisites

- **Python 3.8** or higher
- **pip** (Python package manager)
- **Git** (for cloning the repository)
- **Google AI API Key** (Gemini)

### 🔧 Setup Steps

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/MustafaKocamann/Video-Summarizer-with-Phidata.git
cd Video-Summarizer-with-Phidata
```

#### 2️⃣ Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` and add your Google API key:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

**Get your API key:** https://makersuite.google.com/app/apikey

#### 5️⃣ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📖 Usage Guide

### 🎯 Step-by-Step Tutorial

1. **📤 Upload Video**
   - Click on the upload area
   - Select a video file (MP4, MOV, or AVI)
   - Wait for the upload confirmation

2. **❓ Ask a Question**
   - Type your question in the text area
   - Examples:
     - "Summarize the main points of this video"
     - "What are the key topics discussed?"
     - "Explain the concepts presented in detail"

3. **🔍 Analyze**
   - Click the "🔍 Analyze Video" button
   - Watch the progress bar as the AI processes
   - Sit back and let AI work its magic ✨

4. **📊 Get Results**
   - View comprehensive analysis results
   - Results include AI insights and web research
   - Results are displayed in a clean, readable format

### 💡 Example Queries

```
• What is the main topic of this video?
• Summarize the video in bullet points
• What are the key takeaways?
• Provide a detailed analysis of the content
• What makes this content valuable?
• Explain technical concepts mentioned
```

---

## 🛠 Technology Stack

### 🎨 **Frontend**
- **Streamlit** - Interactive web framework for Python
- **CSS/HTML** - Custom styling and animations
- **Inter Font** - Professional typography

### 🤖 **AI & ML**
- **Google Gemini 2.5 Flash** - Advanced AI model for video analysis
- **Google Generative AI** - Video processing and understanding
- **Phidata** - AI agent framework

### 🔍 **Search & Research**
- **DuckDuckGo Search** - Privacy-focused web search
- **Web Research Integration** - Automatic research capabilities

### ⚙️ **Utilities**
- **Python-dotenv** - Environment variable management
- **FFmpeg** - Video processing and handling

---

## 📁 Project Structure

```
Video-Summarizer-with-Phidata/
│
├── 📄 app.py                    # Main Streamlit application
├── 📋 requirements.txt          # Python dependencies
├── 📖 README.md                 # Project documentation
├── 🔒 .env.example              # Environment variables example
├── 📌 .gitignore                # Git ignore rules
├── ⚙️ runtime.txt               # Python runtime version
├── 📦 packages.txt              # System packages (ffmpeg)
│
└── 📁 .streamlit/
    └── config.toml              # Streamlit configuration
```

---

## ⚙️ Configuration

### Streamlit Configuration (`.streamlit/config.toml`)

```toml
[theme]
primaryColor = "#3b82f6"
backgroundColor = "#0f172a"
secondaryBackgroundColor = "#1e293b"
textColor = "#e2e8f0"
font = "sans serif"

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = true
```

### Environment Variables

Required environment variables in `.env`:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## 🌐 Deployment

### 🚀 Deploy to Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

2. **Connect to Streamlit Cloud**
   - Go to https://share.streamlit.io/
   - Click "New app"
   - Connect your GitHub account
   - Select repository and branch

3. **Add Secrets**
   - In Streamlit Cloud dashboard
   - Go to "Secrets"
   - Add `GOOGLE_API_KEY`

4. **Deploy!**
   - Click Deploy
   - Wait for the app to be live

### 🐳 Docker Deployment (Optional)

```bash
# Build Docker image
docker build -t video-summarizer .

# Run container
docker run -p 8501:8501 -e GOOGLE_API_KEY=your_key video-summarizer
```

---

## 📦 Dependencies

### Core Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | >=1.28.0 | Web framework |
| phidata | >=2.0.0 | AI agent framework |
| google-generativeai | >=0.3.0 | Gemini AI API |
| duckduckgo-search | >=4.0.0 | Web search |
| python-dotenv | >=1.0.0 | Env management |

All dependencies are listed in `requirements.txt`

---

## 🤝 Contributing

### We Welcome Contributions! 🎉

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Video-Summarizer-with-Phidata.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Make your changes**
   - Code your improvements
   - Test thoroughly
   - Follow Python best practices

4. **Commit your changes**
   ```bash
   git commit -m 'Add AmazingFeature'
   ```

5. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

6. **Open a Pull Request**
   - Describe your changes
   - Reference any issues
   - Wait for review

### 📝 Contribution Guidelines

- Follow PEP 8 style guide
- Add comments for complex code
- Test your changes before submitting
- Update README if needed
- Keep commits clean and descriptive

---

## 🐛 Troubleshooting

### 🔴 Common Issues & Solutions

#### Issue: API Key Not Found
```
Solution: Make sure .env file exists with GOOGLE_API_KEY
Check: echo $GOOGLE_API_KEY (should show your key)
```

#### Issue: Video Upload Fails
```
Solution: Ensure video format is MP4, MOV, or AVI
Check: File size should be under Streamlit limits
```

#### Issue: Slow Analysis
```
Solution: This is normal - Gemini needs time to analyze
Try: Restarting the application
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**You are free to:**
- ✅ Use commercially
- ✅ Modify the code
- ✅ Distribute the software
- ✅ Use privately

**With the condition:**
- 📋 Include license and copyright notice

---

## 👨‍💻 Author

### Mustafa Kocaman

**Connect with me:**

- 🐙 **GitHub:** [@MustafaKocamann](https://github.com/MustafaKocamann)
- 💼 **LinkedIn:** [Mustafa Kocaman](https://linkedin.com/in/mustafa-kocaman)
- 📧 **Email:** [mustafakocaman@email.com](mailto:mustafakocaman@email.com)

---

## 🙏 Acknowledgments

**Special thanks to:**

- 🎯 **Google** - For Gemini AI and excellent APIs
- 🔍 **DuckDuckGo** - For privacy-focused search
- 🚀 **Streamlit** - For amazing web framework
- 📚 **Phidata** - For AI agent framework
- 💫 **Open Source Community** - For inspiration and support

---

## 📞 Support

### Need Help? 🤔

- 📖 Check the [Usage Guide](#-usage-guide)
- 🔍 Search [GitHub Issues](https://github.com/MustafaKocamann/Video-Summarizer-with-Phidata/issues)
- 💬 Create a new issue if problem persists
- 📧 Contact me directly

---

## 🚀 Roadmap

### 🔮 Future Features

- [ ] 📁 Batch video processing
- [ ] 📈 Analysis history and export
- [ ] 🎯 Custom analysis templates
- [ ] 🌍 Multi-language support
- [ ] 🎨 More theme options
- [ ] 💾 Cloud storage integration
- [ ] 🔐 User authentication

---

## 📊 Statistics

- ⭐ **Stars:** [Star on GitHub!](https://github.com/MustafaKocamann/Video-Summarizer-with-Phidata)
- 🍴 **Forks:** [Fork it!](https://github.com/MustafaKocamann/Video-Summarizer-with-Phidata/fork)
- 👀 **Watchers:** Keep watching for updates
- 📈 **Growing Community**

---

## 📜 Changelog

### v1.0.0 (January 2026)
- ✨ Initial release
- 🎨 Professional UI with dark theme
- 🤖 Gemini AI integration
- 🔍 DuckDuckGo search integration
- 📊 Real-time progress tracking

---

<div align="center">

### ⭐ If you found this project helpful, please give it a star! ⭐

**Made with ❤️ by [Mustafa Kocaman](https://github.com/MustafaKocamann)**

**[⬆ Back to top](#-video-ai-summarizer)**

</div>
