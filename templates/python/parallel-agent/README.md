# Parallel Agent Template

Agents parallèles pour recherche multi-sources avec fusion des résultats.

## Architecture

```
User → Runner → SequentialAgent → [ParallelAgent → Merger] → Response
                └─> [Researcher1, Researcher2, Researcher3] (parallèle)
```

## Installation

```bash
poetry install
```

## Utilisation

```python
from src.parallel_agent.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

session_service = InMemorySessionService()
runner = Runner(
    agent=root_agent,
    app_name="parallel_agent",
    session_service=session_service
)

content = types.Content(
    role='user',
    parts=[types.Part(text="Research renewable energy trends")]
)

events = runner.run(
    user_id="user123",
    session_id="session001",
    new_message=content
)
```

## Cas d'usage

- Recherche multi-sources
- Analyse comparative
- Tâches indépendantes parallèles
