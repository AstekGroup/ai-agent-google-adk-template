# Référence API Google ADK

## Agents

### Agent (LlmAgent)

Agent principal alimenté par un LLM.

#### Python

```python
from google.adk.agents import Agent

agent = Agent(
    model="gemini-2.0-flash",        # Requis : Modèle LLM
    name="agent_name",               # Requis : Nom de l'agent
    instruction="...",                # Requis : Instructions système
    description="...",                # Optionnel : Description pour délégation
    tools=[...],                      # Optionnel : Liste d'outils
    sub_agents=[...],                # Optionnel : Sous-agents
    planner=...,                     # Optionnel : Planificateur
    input_schema=...,                # Optionnel : Schéma d'entrée
    output_schema=...,               # Optionnel : Schéma de sortie
    output_key="...",                # Optionnel : Clé pour stocker résultat
    generate_content_config=...,     # Optionnel : Config génération
    before_agent_callback=...,       # Optionnel : Callback avant exécution
    after_agent_callback=...,        # Optionnel : Callback après exécution
)
```

#### Java

```java
LlmAgent agent = LlmAgent.builder()
    .model("gemini-2.0-flash")
    .name("agent_name")
    .instruction("...")
    .description("...")
    .tools(...)
    .subAgents(...)
    .build();
```

### SequentialAgent

Exécute des agents dans un ordre séquentiel.

```python
from google.adk.agents import SequentialAgent

sequential = SequentialAgent(
    name="pipeline",
    sub_agents=[agent1, agent2, agent3],
    description="..."
)
```

### ParallelAgent

Exécute des agents en parallèle.

```python
from google.adk.agents import ParallelAgent

parallel = ParallelAgent(
    name="parallel_research",
    sub_agents=[agent1, agent2, agent3],
    description="..."
)
```

### LoopAgent

Exécute des agents en boucle jusqu'à condition.

```python
from google.adk.agents import LoopAgent

loop = LoopAgent(
    name="refinement_loop",
    sub_agents=[critic, refiner],
    max_iterations=5
)
```

### BaseAgent (Custom)

Pour créer des agents personnalisés.

```python
from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event

class CustomAgent(BaseAgent):
    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        # Logique personnalisée
        yield Event(...)
```

## Runners

### Runner

Exécute les agents et gère leur cycle de vie.

```python
from google.adk.runners import Runner

runner = Runner(
    agent=agent,
    app_name="my_app",
    session_service=session_service
)

# Exécution synchrone
events = runner.run(
    user_id="user123",
    session_id="session001",
    new_message=content
)

# Exécution asynchrone
async for event in runner.run_async(
    user_id="user123",
    session_id="session001",
    new_message=content
):
    # Traiter l'événement
    pass
```

### InMemoryRunner

Runner avec gestion de session en mémoire.

```python
from google.adk.runners import InMemoryRunner

runner = InMemoryRunner(agent, app_name="my_app")
session = runner.session_service().create_session(
    "my_app", "user123", "session001"
).blocking_get()
```

## Sessions

### SessionService

Gère les sessions utilisateur.

```python
from google.adk.sessions import InMemorySessionService

session_service = InMemorySessionService()

# Créer une session
session = session_service.create_session(
    app_name="my_app",
    user_id="user123",
    session_id="session001",
    state={"key": "value"}  # État initial optionnel
)

# Récupérer une session
session = session_service.get_session(
    app_name="my_app",
    user_id="user123",
    session_id="session001"
)

# Accéder à l'état
state = session.state
state["key"] = "new_value"
```

## Outils

### FunctionTool

Crée un outil à partir d'une fonction Python.

```python
from google.adk.tools import FunctionTool

def my_function(param: str) -> dict:
    """Description de l'outil."""
    return {"result": "value"}

tool = FunctionTool(my_function)
```

### AgentTool

Utilise un agent comme outil.

```python
from google.adk.tools.agent_tool import AgentTool

agent_tool = AgentTool(agent=sub_agent)
```

### RemoteA2aAgent

Agent distant via protocole A2A.

```python
from google.adk.a2a import RemoteA2aAgent

remote_agent = RemoteA2aAgent(
    name="remote_agent",
    agent_card_url="http://localhost:8001/.well-known/agent-card.json",
    description="..."
)
```

## Memory

### MemoryService

Gère la mémoire persistante.

```python
from google.adk.memory import InMemoryMemoryService
from google.adk.tools import load_memory

memory_service = InMemoryMemoryService()

# Ajouter à la mémoire
memory_service.add(
    app_name="my_app",
    user_id="user123",
    content=types.Content(...)
)

# Charger depuis la mémoire
memory = load_memory(
    query="recherche",
    memory_service=memory_service,
    app_name="my_app",
    user_id="user123"
)
```

## Exemples

### BaseExampleProvider

Fournit des exemples pour l'apprentissage.

```python
from google.adk.examples import BaseExampleProvider
from google.adk.examples import Example

class MyExampleProvider(BaseExampleProvider):
    def get_examples(self, query: str):
        return [
            Example(
                input=types.Content(...),
                output=[types.Content(...)]
            )
        ]

# Utiliser avec un agent
agent = Agent(
    ...,
    example_provider=MyExampleProvider()
)
```

## Planification

### BuiltInPlanner

Planificateur intégré avec thinking.

```python
from google.adk.planners import BuiltInPlanner
from google.genai import types

thinking_config = types.ThinkingConfig(
    include_thoughts=True,
    thinking_budget=256
)

planner = BuiltInPlanner(thinking_config=thinking_config)

agent = Agent(
    ...,
    planner=planner
)
```

## Configuration de génération

### GenerateContentConfig

Contrôle les paramètres de génération LLM.

```python
from google.genai import types

config = types.GenerateContentConfig(
    temperature=0.2,
    max_output_tokens=250,
    top_p=0.95,
    top_k=40,
    safety_settings=[
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
        )
    ]
)

agent = Agent(..., generate_content_config=config)
```

## Callbacks

### CallbackContext

Contexte pour les callbacks avant/après exécution.

```python
from google.adk.agents.callback_context import CallbackContext

def before_agent_callback(ctx: CallbackContext):
    # Accéder au contexte
    agent_name = ctx._invocation_context.agent.name
    session_id = ctx._invocation_context.session.id
    
    # Modifier l'état
    ctx.state["key"] = "value"
    
    # Modifier les instructions
    ctx._invocation_context.agent.instruction += "\nAdditional context"

agent = Agent(
    ...,
    before_agent_callback=before_agent_callback
)
```

## Événements

### Event

Événements émis pendant l'exécution.

```python
from google.adk.events import Event

for event in events:
    if event.is_final_response():
        print(event.content)
    elif event.is_tool_call():
        print(event.tool_name, event.tool_args)
```

## Protocole A2A

### Exposer un agent

```python
from google.adk.a2a.utils.agent_to_a2a import to_a2a

a2a_app = to_a2a(agent, port=8001)

# Démarrer avec uvicorn
# uvicorn module.path:a2a_app --host localhost --port 8001
```

### Consommer un agent distant

```python
from google.adk.a2a import RemoteA2aAgent

remote_agent = RemoteA2aAgent(
    name="remote",
    agent_card_url="http://localhost:8001/.well-known/agent-card.json"
)

# Utiliser comme outil
root_agent = Agent(..., tools=[remote_agent])
```
