from langchain_community.chat_models import ChatOllama
from rag_engine import get_retriever
from memory import memory
from crm import save_lead

# Use Ollama
llm = ChatOllama(
    model="mistral",
    temperature=0.4
)

retriever = get_retriever()

SYSTEM_PROMPT = """
You are an AI Sales + Customer Success Agent.

Your responsibilities:
- Understand if the client is new or existing
- Be empathetic and conversational
- Help in sales, support, upsell, cross-sell, retention
- Suggest upgrades smartly
- Handle objections like pricing concerns
- Never hallucinate pricing or features
- If feature not available:
    → suggest workaround
    → or offer customization (no timeline)

Sales Behavior:
- Ask questions before pitching
- Be consultative, not pushy
- Always aim to maximize customer value
"""

def retrieve_context(query):
    try:
        docs = retriever.invoke(query)
        return "\n".join([doc.page_content[:300] for doc in docs])
    except:
        return ""

def classify_intent(message):
    msg = message.lower()
    if any(x in msg for x in ["price", "cost", "plan"]):
        return "pricing"
    elif any(x in msg for x in ["cancel", "refund", "not happy"]):
        return "retention"
    elif any(x in msg for x in ["feature", "integration"]):
        return "feature_query"
    elif any(x in msg for x in ["upgrade", "premium"]):
        return "upsell"
    elif any(x in msg for x in ["problem", "issue", "error"]):
        return "support"
    else:
        return "general"

def agent_response(session_id, user_message):
    print("📩 Incoming:", session_id, user_message)

    # ✅ SAVE LEAD (FIXED)
    save_lead(session_id, user_message)

    user_context = memory.get(session_id)
    intent = classify_intent(user_message)
    knowledge = retrieve_context(user_message)

    prompt = f"""
{SYSTEM_PROMPT}

User Context:
{user_context}

Detected Intent: {intent}

Relevant Knowledge:
{knowledge}

User Message:
{user_message}

Instructions:
- If NEW client → ask requirements first
- If EXISTING → solve issue first, then upsell if relevant
- If pricing concern → justify value + offer retention strategy
- If feature missing → workaround or customization
- Be human, empathetic, and persuasive
"""

    response = llm.invoke(prompt)

    # Save memory
    memory.update(session_id, "last_intent", intent)
    memory.update(session_id, "last_message", user_message)

    return response.content