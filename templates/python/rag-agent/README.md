# RAG Agent Template

Agent avec intégration Vertex AI RAG pour Q&A sur documentation.

## Architecture

```
User → Runner → RAG Agent → RAG Tool → Vector Search → Context → Response
```

## Prérequis

- Vertex AI RAG Corpus configuré
- Variable d'environnement RAG_CORPUS pointant vers le corpus

## Installation

```bash
poetry install
```

## Configuration

```bash
cp env.example .env
# Éditer .env avec vos valeurs, notamment RAG_CORPUS
```

## Utilisation

```python
from src.rag_agent.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

session_service = InMemorySessionService()
runner = Runner(
    agent=root_agent,
    app_name="rag_agent",
    session_service=session_service
)

content = types.Content(
    role='user',
    parts=[types.Part(text="What are the key features of BigQuery?")]
)

events = runner.run(
    user_id="user123",
    session_id="session001",
    new_message=content
)
```

## Cas d'usage

- Q&A sur documentation
- Recherche contextuelle
- Agents avec connaissances spécialisées
