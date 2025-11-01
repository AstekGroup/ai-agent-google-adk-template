# Simple Agent Template

Agent Google ADK simple avec un outil de météo.

## Installation

```bash
poetry install
# ou
uv sync
```

## Configuration

```bash
cp .env.example .env
# Éditer .env avec vos valeurs
```

## Utilisation

```python
from src.simple_agent.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

session_service = InMemorySessionService()
session = session_service.create_session(
    app_name="simple_agent",
    user_id="user123",
    session_id="session001"
)

runner = Runner(
    agent=root_agent,
    app_name="simple_agent",
    session_service=session_service
)

content = types.Content(
    role='user',
    parts=[types.Part(text="What's the weather in Paris?")]
)

events = runner.run(
    user_id="user123",
    session_id="session001",
    new_message=content
)

for event in events:
    if event.is_final_response() and event.content:
        print(event.content.parts[0].text)
```

## Tests

```bash
pytest tests/
```

## Déploiement

```bash
cd deployment
python deploy.py --create
```
