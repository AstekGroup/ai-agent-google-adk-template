# Architecture et concepts du Google ADK

## Types d'agents

### 1. LlmAgent (Agent LLM)
Agent intelligent alimenté par un modèle de langage (LLM) pour la prise de décision intelligente.

```python
from google.adk.agents import Agent

agent = Agent(
    model="gemini-2.0-flash",
    name="my_agent",
    instruction="You are a helpful assistant.",
    tools=[...]
)
```

### 2. SequentialAgent (Agent séquentiel)
Exécute plusieurs agents dans un ordre fixe et déterminé pour des processus structurés.

```python
from google.adk.agents import SequentialAgent

pipeline = SequentialAgent(
    name="pipeline",
    sub_agents=[agent1, agent2, agent3]
)
```

### 3. ParallelAgent (Agent parallèle)
Exécute plusieurs agents simultanément pour des tâches indépendantes afin de maximiser les performances.

```python
from google.adk.agents import ParallelAgent

parallel_agent = ParallelAgent(
    name="parallel_research",
    sub_agents=[researcher1, researcher2, researcher3]
)
```

### 4. LoopAgent (Agent en boucle)
Exécute des agents de manière répétée jusqu'à ce qu'une condition de terminaison soit remplie pour des workflows d'amélioration itératifs.

```python
from google.adk.agents import LoopAgent

refinement_loop = LoopAgent(
    name="refinement_loop",
    sub_agents=[critic_agent, refiner_agent],
    max_iterations=5
)
```

### 5. BaseAgent / Custom Agent
Permet d'étendre BaseAgent pour implémenter une logique d'orchestration personnalisée au-delà des patterns de workflow prédéfinis.

## Composants principaux

### Runner
Composant qui exécute les agents et gère leur cycle de vie.

```python
from google.adk.runners import Runner

runner = Runner(
    agent=agent,
    app_name="my_app",
    session_service=session_service
)
```

### Session Service
Gère les sessions utilisateur et l'état de l'agent.

```python
from google.adk.sessions import InMemorySessionService

session_service = InMemorySessionService()
session = session_service.create_session(
    app_name="my_app",
    user_id="user123",
    session_id="session001"
)
```

### Memory Service
Gère la mémoire persistante des agents.

```python
from google.adk.memory import InMemoryMemoryService

memory_service = InMemoryMemoryService()
```

### Tools
Outils que les agents peuvent utiliser pour interagir avec le monde extérieur.

```python
from google.adk.tools import FunctionTool

def my_tool(param: str) -> dict:
    """Tool description."""
    return {"result": "value"}

tool = FunctionTool(my_tool)
```

## Modèles d'orchestration

### 1. Workflow séquentiel
Exécution étape par étape dans un ordre déterminé.

```
Agent1 → Agent2 → Agent3 → Résultat final
```

### 2. Workflow parallèle
Exécution simultanée de plusieurs agents indépendants.

```
    → Agent1 ─┐
    → Agent2 ─┼→ Merger Agent → Résultat
    → Agent3 ─┘
```

### 3. Workflow en boucle
Itération jusqu'à satisfaction d'une condition.

```
Initial Agent → [Critic → Refiner] (loop) → Final Agent
```

### 4. Workflow conditionnel
Exécution basée sur des conditions dynamiques.

```
Agent → Condition Check → Branch A or Branch B
```

## Agent2Agent (A2A) Protocol

Protocole permettant la communication entre agents distribués sur des réseaux.

### Exposer un agent en A2A

```python
from google.adk.a2a.utils.agent_to_a2a import to_a2a

a2a_app = to_a2a(agent, port=8001)
```

### Consommer un agent distant

```python
from google.adk.a2a import RemoteA2aAgent

remote_agent = RemoteA2aAgent(
    name="remote_agent",
    agent_card_url="http://localhost:8001/.well-known/agent-card.json"
)
```

## Gestion d'état

### Session State
État persistant par session utilisateur.

```python
session.state["key"] = "value"
```

### Invocation Context
Contexte d'invocation pour chaque exécution d'agent.

```python
ctx.session.state.get("key")
ctx.agent.name
ctx.invocation_id
```

## Événements et streaming

Les agents émettent des événements pendant l'exécution :

```python
for event in runner.run(...):
    if event.is_final_response():
        print(event.content)
```

Types d'événements :
- `agent_start`
- `tool_call`
- `agent_response`
- `final_response`

## Intégration des modèles LLM

### Google Gemini

```python
agent = Agent(model="gemini-2.0-flash", ...)
```

### Vertex AI

```python
# Configuration via variables d'environnement
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=your-project
GOOGLE_CLOUD_LOCATION=us-central1
```

### Autres LLMs via LiteLLM

```python
from google.adk.models.lite_llm import LiteLlm

agent = Agent(
    model=LiteLlm(model="openai/gpt-4o"),
    ...
)
```

## Configuration de génération

```python
from google.genai import types

agent = Agent(
    model="gemini-2.0-flash",
    generate_content_config=types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=250,
        top_p=0.95,
        safety_settings=[...]
    )
)
```

## Planification

### Built-in Planner

```python
from google.adk.planners import BuiltInPlanner

planner = BuiltInPlanner(
    thinking_config=types.ThinkingConfig(
        include_thoughts=True,
        thinking_budget=256
    )
)

agent = Agent(planner=planner, ...)
```

## Schémas structurés

Définir des schémas d'entrée/sortie pour la sécurité des types.

```python
from pydantic import BaseModel

class InputSchema(BaseModel):
    field: str

class OutputSchema(BaseModel):
    result: str

agent = Agent(
    input_schema=InputSchema,
    output_schema=OutputSchema,
    ...
)
```
