# 🤖 GramAI

GramAI is the AI intelligence layer for **Grambazer**, a local marketplace and community platform.

GramAI combines:

- FastAPI
- Python
- MongoDB
- Redis
- Qdrant
- Ollama
- LLMs
- RAG
- AI Agents
- Tool Calling
- Conversation Memory
- Seller Intelligence
- Marketing Generation

---

# Architecture

```text
                    ┌───────────────────┐
                    │   React / Mobile  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │      FastAPI      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   AI Orchestrator │
                    └─────────┬─────────┘
                              │
                ┌─────────────┼─────────────┐
                ▼             ▼             ▼
             Planner       Tools          Memory
                │             │             │
                ▼             ▼             ▼
              LLM         MongoDB        Qdrant
                              │
                              ▼
                           Redis
```