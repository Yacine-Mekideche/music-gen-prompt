# 🎵 IAcine MusicGen | AI-Powered Music Generator From Prompt

![image](https://github.com/user-attachments/assets/d3ded334-a435-4374-b132-408b16530f99)



## 📖 Introduction

**IAcine MusicGen** is a lightweight, AI-powered application that turns simple text prompts into original music. Built using OpenAI and Meta’s MusicGen model, this tool transforms creative ideas into audio — instantly and interactively. Whether you're a musician, content creator, or AI enthusiast, this project shows how AI can be used to generate melodies from scratch. 🧠🎶

Accessible via a **simple Streamlit interface**, users can describe a musical idea (e.g., "calm lo-fi with rain") and instantly receive an original track.


## 🚀 Features

✔️ **Prompt-to-Music Generation** – Describe a style, vibe, or mood, and get a custom audio track 🎤➡️🎼  
✔️ **Streamlit Web Interface** – Clean and simple UI for interaction with the model  
✔️ **AI Prompt Engineering** – Uses GPT to interpret user input into optimized music prompts  
✔️ **Duration Control** – Choose between different durations (5s, 10s, 30s...)  
✔️ **Local Generation** – All processing runs locally (ideal for testing and demos)


## 🏗️ Technologies

- 🐍 **Python 3.12** – Backend logic and interface
- 🧠 **OpenAI GPT-3.5** – For generating high-quality music prompts
- 🎵 **Meta MusicGen** – For transforming prompts into original audio
- 🌐 **Streamlit** – Fast UI development for interaction
- 🛡️ **dotenv** – Environment variable management (for API keys)


## 📦 Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Yacine-Mekideche/music-gen-prompt.git
cd music-gen-prompt
```

### **2️⃣ Create a `.env` File**
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### **3️⃣ Set Up Your Environment**
```bash
python -m venv venv
# Activate it:
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### **4️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```


## ▶️ Running the App

Simply run:
```bash
streamlit run app.py
```

This will open the Streamlit interface in your browser. Enter a musical idea (e.g., "sad piano ballad with ambient background") and enjoy the generated music 🎧


## 🎯 Demo

<a href="https://www.youtube.com/watch?v=Nvwsaab2A4Q" target="_blank">
  <img src="https://img.youtube.com/vi/Nvwsaab2A4Q/maxresdefault.jpg" alt="IAcine MusicGen Demo Video" style="max-width:100%; height:auto;">
</a>


## 🧠 AI Architecture Overview

- **Text Input** → Interpreted by GPT into structured music prompt  
- **Prompt** → Sent to MusicGen model for waveform generation  
- **Audio Output** → Played back through Streamlit UI  


## 📬 Contact Me

💡 **Interested in AI + Creativity? Let's connect!**

[![Website](https://img.shields.io/badge/My%20Website-%23000000.svg?style=for-the-badge&logo=About.me&logoColor=white)](https://iacine.tech)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yacine-mekideche/)  
[![GitHub](https://img.shields.io/badge/GitHub-%2312100E.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Yacine-Mekideche)  
[![Malt](https://img.shields.io/badge/Malt-%23FF6F61.svg?style=for-the-badge&logo=malt&logoColor=white)](https://malt.fr/profile/yacinemekideche)  
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@iacine_tech)  

📩 **Business inquiries:** contact@iacine.tech

---

**#AI #MusicGen #PromptToMusic #Streamlit #Python #OpenAI #MetaAI #GenerativeAI #MusicAI #IAcineTech #CreativeAI #TextToMusic #ArtificialIntelligence**
