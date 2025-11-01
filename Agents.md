# Agents.md - Guide pour les IA développant avec Google ADK

**Date de mise à jour : Novembre 2025**

Ce document fournit des instructions complètes aux assistants IA pour créer, développer et maintenir des agents Google ADK dans différents langages.

## Vue d'ensemble

Google Agent Development Kit (ADK) est un framework open-source pour construire des agents IA sophistiqués. Il supporte Python et Java, avec des patterns d'orchestration avancés, des outils modulaires, et un déploiement flexible.

## Principes fondamentaux

### 1. Architecture des agents

- **LlmAgent** : Agent de base alimenté par un LLM (Gemini, OpenAI, Claude, etc.)
- **SequentialAgent** : Exécution séquentielle d'agents
- **ParallelAgent** : Exécution parallèle d'agents indépendants
- **LoopAgent** : Exécution itérative jusqu'à condition de sortie
- **BaseAgent** : Agent personnalisé pour logique d'orchestration spécifique

### 2. Composants essentiels

- **Runner** : Exécute les agents et gère leur cycle de vie
- **SessionService** : Gère les sessions utilisateur et l'état persistant
- **MemoryService** : Gère la mémoire à long terme des agents
- **Tools** : Outils modulaires pour interactions externes

### 3. Gestion d'état

- Utiliser `session.state` pour stocker l'état de session
- Utiliser `callback_context.state` dans les callbacks
- Préfixer avec `user:` pour les artefacts utilisateur

## Structure de projet recommandée

### Python

```
project-name/
├── pyproject.toml          # Configuration du projet (Poetry/uv)
├── README.md               # Documentation du projet
├── .env.example           # Exemple de variables d'environnement
├── .env                    # Variables d'environnement (non versionné)
├── src/
│   └── agent_name/
│       ├── __init__.py
│       ├── agent.py        # Définition de l'agent principal
│       ├── tools/          # Outils personnalisés
│       │   ├── __init__.py
│       │   └── custom_tools.py
│       ├── sub_agents/     # Sous-agents (si multi-agent)
│       │   ├── __init__.py
│       │   └── specialized_agent.py
│       └── callbacks/      # Callbacks personnalisés
│           ├── __init__.py
│           └── state_callbacks.py
├── tests/
│   ├── __init__.py
│   ├── test_agent.py       # Tests unitaires
│   └── test_tools.py
├── eval/                   # Évaluations
│   └── data/
│       └── test_cases.json
├── deployment/
│   ├── deploy.py          # Script de déploiement
│   ├── test_deployment.py
│   └── Dockerfile         # (optionnel pour Cloud Run)
└── docs/                  # Documentation additionnelle
    └── architecture.md
```

### Java

```
project-name/
├── pom.xml                 # Configuration Maven
├── README.md
├── .env.example
├── src/
│   └── main/
│       ├── java/
│       │   └── com/google/adk/samples/agent/
│       │       ├── Agent.java           # Agent principal
│       │       ├── Main.java            # Point d'entrée
│       │       ├── tools/               # Outils personnalisés
│       │       ├── subagents/           # Sous-agents
│       │       └── services/            # Services métier
│       └── resources/
│           ├── application.properties
│           └── prompts/                # Templates de prompts
└── test/
    └── java/
        └── com/google/adk/samples/agent/
            └── AgentTest.java
```

## Patterns d'implémentation

### Pattern 1 : Agent simple avec outils

**Python** :
```python
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

def my_tool(param: str) -> dict:
    """Description de l'outil."""
    return {"result": "value"}

agent = Agent(
    model="gemini-2.5-flash",
    name="my_agent",
    instruction="Instructions système pour l'agent.",
    description="Description pour délégation multi-agent",
    tools=[FunctionTool(my_tool)]
)

session_service = InMemorySessionService()
runner = Runner(
    agent=agent,
    app_name="my_app",
    session_service=session_service
)
```

**Java** :
```java
import com.google.adk.agents.LlmAgent;
import com.google.adk.runner.InMemoryRunner;
import com.google.adk.sessions.Session;
import com.google.genai.types.Content;
import com.google.genai.types.Part;

LlmAgent agent = LlmAgent.builder()
    .model("gemini-2.5-flash")
    .name("my_agent")
    .instruction("Instructions système pour l'agent.")
    .description("Description pour délégation multi-agent")
    .tools(myTool)
    .build();

InMemoryRunner runner = new InMemoryRunner(agent, "my_app");
```

### Pattern 2 : Multi-agent séquentiel

```python
from google.adk.agents import Agent, SequentialAgent

agent1 = Agent(name="writer", ...)
agent2 = Agent(name="reviewer", ...)
agent3 = Agent(name="refiner", ...)

pipeline = SequentialAgent(
    name="writing_pipeline",
    sub_agents=[agent1, agent2, agent3]
)
```

### Pattern 3 : Multi-agent parallèle

```python
from google.adk.agents import Agent, ParallelAgent

researcher1 = Agent(name="research_1", ...)
researcher2 = Agent(name="research_2", ...)
researcher3 = Agent(name="research_3", ...)

parallel_research = ParallelAgent(
    name="parallel_research",
    sub_agents=[researcher1, researcher2, researcher3]
)
```

### Pattern 4 : Boucle d'amélioration

```python
from google.adk.agents import Agent, LoopAgent
from google.adk.tools import ToolContext

def exit_loop(tool_context: ToolContext):
    tool_context.actions.escalate = True
    return {}

critic = Agent(name="critic", ...)
refiner = Agent(name="refiner", tools=[exit_loop], ...)

refinement_loop = LoopAgent(
    name="refinement_loop",
    sub_agents=[critic, refiner],
    max_iterations=5
)
```

## Callbacks et gestion d'état

### Callbacks avant exécution

```python
from google.adk.agents.callback_context import CallbackContext

def before_agent_callback(ctx: CallbackContext):
    # Initialiser l'état
    if "user_preferences" not in ctx.state:
        ctx.state["user_preferences"] = {}
    
    # Modifier les instructions dynamiquement
    if ctx.state.get("lang") == "fr":
        ctx._invocation_context.agent.instruction += "\nRépondez en français."
    
    return None

agent = Agent(
    ...,
    before_agent_callback=before_agent_callback
)
```

### Callbacks après exécution

```python
def after_agent_callback(ctx: CallbackContext):
    # Logger les résultats
    response = ctx._invocation_context.response
    ctx.state["last_response"] = response
    
    # Mettre à jour les métriques
    ctx.state["turn_count"] = ctx.state.get("turn_count", 0) + 1
    
    return None
```

## Outils personnalisés

### Outil synchrone

```python
from google.adk.tools import FunctionTool
from typing import Literal

def get_weather(
    city: str,
    units: Literal["celsius", "fahrenheit"] = "celsius"
) -> dict:
    """
    Récupère la météo pour une ville.
    
    Args:
        city: Nom de la ville
        units: Unités de température
    
    Returns:
        Dict avec status, temperature, condition
    """
    # Implémentation
    return {
        "status": "success",
        "city": city,
        "temperature": "25",
        "units": units,
        "condition": "sunny"
    }

weather_tool = FunctionTool(get_weather)
```

### Outil asynchrone

```python
import asyncio
from google.adk.tools import FunctionTool

async def async_api_call(endpoint: str) -> dict:
    """Appel API asynchrone."""
    await asyncio.sleep(0.5)
    return {"status": "success", "data": {}}

async_tool = FunctionTool(async_api_call)
```

## Configuration et variables d'environnement

### Variables essentielles

```bash
# Choix du backend LLM
GOOGLE_GENAI_USE_VERTEXAI=1  # 1 pour Vertex AI, 0 pour AI Studio

# Configuration Vertex AI (production)
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1

# Configuration AI Studio (développement)
GOOGLE_API_KEY=your-api-key

# Configuration application
APP_NAME=my_agent_app
LOG_LEVEL=INFO
```

## Tests et évaluation

### Test unitaire Python

```python
import pytest
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent_name.agent import root_agent

def test_agent_basic():
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name="test_app",
        session_service=session_service
    )
    
    session = session_service.create_session(
        app_name="test_app",
        user_id="test_user",
        session_id="test_session"
    )
    
    content = types.Content(
        role='user',
        parts=[types.Part(text="Hello")]
    )
    
    events = runner.run(
        user_id="test_user",
        session_id="test_session",
        new_message=content
    )
    
    final_responses = [
        e for e in events if e.is_final_response()
    ]
    
    assert len(final_responses) > 0
```

## Déploiement

### Vertex AI Agent Engine

1. Construire le package :
   ```bash
   # Python
   poetry build --format=wheel --out-dir deployment
   # ou
   uv build --wheel --out-dir deployment
   
   # Java
   mvn clean package
   ```

2. Déployer :
   ```python
   from vertexai import agent_engines
   import os
   
   reasoning_engine = agent_engines.ReasoningEngine.create(
       reasoning_engine={
           "display_name": "my-agent",
           "model_config": {"model": "gemini-2.5-flash"},
           "source": {
               "package_path": "deployment/my_agent-1.0.0-py3-none-any.whl",
               "entrypoint": "agent_name.agent:root_agent",
           },
       }
   )
   ```

### Cloud Run

```dockerfile
FROM python:3.11-slim

RUN pip install --no-cache-dir uv==0.6.12

WORKDIR /code

COPY ./pyproject.toml ./README.md ./uv.lock* ./
COPY ./src ./src

RUN uv sync --frozen

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Best Practices

### 1. Instructions claires

- Instructions système précises et concises
- Décrire les capacités et limites de l'agent
- Fournir des exemples de comportement attendu

### 2. Gestion d'erreurs

- Implémenter des retries avec backoff exponentiel
- Gérer gracieusement les erreurs d'outils
- Fournir des messages d'erreur clairs à l'utilisateur

### 3. Performance

- Utiliser ParallelAgent pour tâches indépendantes
- Mettre en cache les résultats coûteux
- Limiter les itérations dans LoopAgent

### 4. Sécurité

- Valider les entrées utilisateur
- Sanitizer les réponses avant affichage
- Gérer les secrets via variables d'environnement

### 5. Observabilité

- Logger les événements importants
- Tracker les métriques de performance
- Utiliser les callbacks pour instrumentation

## Ressources de référence

- Documentation officielle : https://google.github.io/adk-docs/
- Exemples : https://github.com/google/adk-samples
- Agent Starter Pack : https://github.com/GoogleCloudPlatform/agent-starter-pack
- Ressources complètes : Voir `resources/` dans ce projet

## Checklist de développement

- [ ] Structure de projet créée selon template
- [ ] Agent principal défini avec instructions claires
- [ ] Outils nécessaires implémentés et testés
- [ ] Gestion d'état configurée (callbacks si nécessaire)
- [ ] Tests unitaires écrits et passants
- [ ] Variables d'environnement documentées (.env.example)
- [ ] README.md complet avec instructions
- [ ] Script de déploiement prêt (si applicable)
- [ ] Documentation API/interfaces complète

## Support et contribution

Pour toute question ou amélioration de ce guide, référez-vous à la documentation dans `resources/` ou aux repositories officiels Google ADK.
