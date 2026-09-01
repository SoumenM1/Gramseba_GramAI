# GramAI Architecture

GramAI is an AI backend for Grambazer.

## Main layers

Client
↓
FastAPI
↓
Services
↓
AI Orchestrator
↓
Tools
↓
MongoDB / Redis / Qdrant
↓
LLM

## AI flow

User message
↓
Input Guard
↓
Planner
↓
Tool selection
↓
Database/API tool
↓
LLM
↓
Output Guard
↓
Response