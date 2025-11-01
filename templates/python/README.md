# Template Python - Agent Google ADK Simple

**Version : 1.0.0**  
**Date : Novembre 2025**  
**Langage : Python 3.11+**

## Description

Template de base pour créer un agent Google ADK en Python. Ce template inclut :
- Configuration avec Poetry ou uv
- Structure de projet standardisée
- Agent simple avec exemple d'outil
- Gestion de session
- Tests de base
- Script de déploiement

## Structure du projet

```
simple-agent-python/
├── pyproject.toml          # Configuration Poetry/uv
├── README.md               # Documentation
├── .env.example           # Exemple de variables d'environnement
├── .gitignore
├── src/
│   └── simple_agent/
│       ├── __init__.py
│       ├── agent.py        # Agent principal
│       └── tools.py        # Outils personnalisés
├── tests/
│   ├── __init__.py
│   └── test_agent.py
├── deployment/
│   ├── deploy.py          # Script de déploiement Vertex AI
│   └── test_deployment.py
└── docs/
    └── README.md
```

## Installation

### Prérequis

- Python 3.11+
- Poetry ou uv
- Clé API Google Gemini (AI Studio) ou compte Vertex AI

### Configuration

1. Cloner ou copier ce template
2. Installer les dépendances :
   ```bash
   # Avec Poetry
   poetry install
   poetry shell
   
   # Avec uv
   uv sync
   source .venv/bin/activate
   ```

3. Configurer les variables d'environnement :
   ```bash
   cp .env.example .env
   # Éditer .env avec vos valeurs
   ```

## Utilisation

### Exécution locale

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
    parts=[types.Part(text="Hello!")]
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

### Tests

```bash
pytest tests/
```

## Déploiement

Voir `deployment/deploy.py` pour le déploiement sur Vertex AI Agent Engine.

```bash
cd deployment
python deploy.py --create
```

## Fichiers clés

### src/simple_agent/agent.py

```python
from google.adk.agents import Agent
from .tools import get_weather_tool

root_agent = Agent(
    model="gemini-2.5-flash",
    name="simple_agent",
    description="Agent simple avec capacité météo",
    instruction="""You are a helpful assistant that can provide weather information.
    When users ask about weather, use the get_weather tool.
    Be friendly and concise in your responses.""",
    tools=[get_weather_tool]
)
```

### src/simple_agent/tools.py

```python
from google.adk.tools import FunctionTool
from typing import Literal

def get_weather(
    city: str,
    units: Literal["celsius", "fahrenheit"] = "celsius"
) -> dict:
    """
    Get current weather for a city.
    
    Args:
        city: City name
        units: Temperature units
    
    Returns:
        Weather information dictionary
    """
    # Mock implementation - replace with real API call
    return {
        "status": "success",
        "city": city,
        "temperature": "25",
        "units": units,
        "condition": "sunny"
    }

get_weather_tool = FunctionTool(get_weather)
```

## Personnalisation

1. Modifier `src/simple_agent/agent.py` pour définir votre agent
2. Ajouter des outils dans `src/simple_agent/tools.py`
3. Adapter les instructions selon votre cas d'usage
4. Modifier les tests dans `tests/test_agent.py`

## Ressources

- [Documentation ADK Python](../resources/04-api-reference.md)
- [Guide de démarrage](../resources/03-getting-started.md)
- [Agents.md](../../Agents.md) pour guide complet aux IA
