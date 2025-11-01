# Loop Agent Template

Boucle d'amélioration itérative : Critic → Refiner jusqu'à satisfaction.

## Architecture

```
User → Runner → SequentialAgent → [Initial Writer → LoopAgent] → Response
                                    └─> [Critic → Refiner]×N (boucle)
```

## Installation

```bash
poetry install
```

## Utilisation

```python
from src.loop_agent.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

session_service = InMemorySessionService()
session = session_service.create_session(
    app_name="loop_agent",
    user_id="user123",
    session_id="session001",
    state={"topic": "A brave kitten exploring a haunted house"}
)

runner = Runner(
    agent=root_agent,
    app_name="loop_agent",
    session_service=session_service
)

content = types.Content(
    role='user',
    parts=[types.Part(text="Generate and refine a story")]
)

events = runner.run(
    user_id="user123",
    session_id="session001",
    new_message=content
)
```

## Cas d'usage

- Refinement de contenu
- Optimisation itérative
- Amélioration jusqu'à critères de qualité
