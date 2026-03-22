# 🤖 AI Sales Agent (Agentic AI System)

An end-to-end **Agentic AI-powered Sales & Customer Success Assistant** that runs locally using **Ollama + FastAPI + React**.

This system acts as a **virtual sales + support representative**, capable of:
- Handling customer queries
- Understanding requirements
- Suggesting plans (upsell / cross-sell)
- Retaining customers
- Managing leads via a CRM dashboard

---

# 🚀 Features

## 🧠 AI Agent Capabilities
- Conversational AI (ChatGPT-like UI)
- Intent detection (pricing, support, retention, upsell)
- Context-aware responses using RAG (Retrieval-Augmented Generation)
- Empathetic and consultative sales behavior
- Handles:
  - New leads (requirement gathering)
  - Existing customers (support + upsell)
  - Feature gaps (workarounds / customization)

---

## 📊 CRM Dashboard
- Track all leads and conversations
- Displays:
  - Session ID
  - User messages
  - Status (New / can be extended to Hot/Warm/Cold)
- Real-time updates (optional polling)

---

## 🎤 Voice Support (Optional)
- Speech-to-text (Whisper)
- Text-to-speech responses

---

## ⚡ Fully Local Setup
- Runs on **Ollama (LLM)**
- No external API dependency
- Data stored locally

---

# 🏗️ Project Structure

ai-sales-agent/
│
├── agent.py # Core AI agent logic
├── main.py # FastAPI backend
├── rag_engine.py # Vector DB + retrieval
├── crm.py # Lead management system
├── memory.py # Session memory
├── voice.py # Voice (STT + TTS)
│
├── data/ # Knowledge base
│ ├── product_features.pdf
│ ├── pricing.txt
│ └── retention.txt
│
├── frontend/ # React frontend
│ ├── src/
│ │ ├── App.js
│ │ ├── Chat.js
│ │ ├── CRM.js
│ │ └── api.js
│
├── requirements.txt
└── README.md


---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/ai-sales-agent.git
cd ai-sales-agent
2️⃣ Backend Setup
Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
Install dependencies
pip install -r requirements.txt
3️⃣ Install Ollama

Download and install:
👉 https://ollama.com

Pull model
ollama pull mistral
4️⃣ Create Vector Database
python -c "from rag_engine import create_vector_store; create_vector_store()"
5️⃣ Run Backend
uvicorn main:app --reload

👉 API will run at:

http://127.0.0.1:8000
6️⃣ Frontend Setup
cd frontend
npm install
npm start

👉 Open:

http://localhost:3000
🌐 Application URLs
Feature	URL
Chat UI	http://localhost:3000

CRM Dashboard	http://localhost:3000/crm

API Docs	http://127.0.0.1:8000/docs

Leads API	http://127.0.0.1:8000/leads
🧪 Example Test Prompts

Try these in chat:

💰 Pricing

"What are your pricing plans?"

"Do you have a cheaper option?"

🚀 Sales

"I need a solution for my startup"

"What features do you offer?"

🔄 Retention

"I want to cancel my subscription"

"This is too expensive"

🛠️ Feature Request

"Do you support WhatsApp integration?"

🧠 How It Works

User sends message via chat UI

FastAPI receives request

Agent:

Detects intent

Retrieves context (RAG)

Generates response via Ollama

Lead is saved in CRM

Response returned to UI

🔥 Future Enhancements

Lead scoring (Hot / Warm / Cold)

Full conversation history per lead

Clickable CRM rows → open chat

Analytics dashboard

Multi-agent architecture

Deployment on cloud (AWS/GCP)

🛠️ Tech Stack

Backend: FastAPI (Python)

Frontend: React.js

LLM: Ollama (Mistral / LLaMA)

Vector DB: Chroma

AI Framework: LangChain

Voice: Whisper (optional)

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

📜 License

This project is open-source and available under the MIT License.

💡 Author

Built by Ayush Srivastava
🚀 Passionate about AI, SaaS, and building agentic systems

⭐ If you like this project

Give it a ⭐ on GitHub and share it!
