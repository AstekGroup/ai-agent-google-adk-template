# Guide de démarrage avec Google ADK

## Installation

### Python

```bash
pip install google-adk
```

### Java

#### Maven
```xml
<dependency>
    <groupId>com.google.adk</groupId>
    <artifactId>google-adk</artifactId>
    <version>1.3.0</version>
</dependency>
```

#### Gradle
```groovy
dependencies {
    implementation 'com.google.adk:google-adk:1.3.0'
}
```

## Configuration de l'environnement

### Option 1 : Google AI Studio (Démarrage facile)

```bash
export GOOGLE_API_KEY="YOUR_API_KEY"
export GOOGLE_GENAI_USE_VERTEXAI="False"
```

Obtenez votre clé API depuis : https://aistudio.google.com/app/apikey

### Option 2 : Vertex AI (Production)

```bash
# Authentification
gcloud auth application-default login
gcloud auth application-default set-quota-project $GOOGLE_CLOUD_PROJECT

# Variables d'environnement
export GOOGLE_GENAI_USE_VERTEXAI="True"
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"
```

## Premier agent simple

### Python

```python
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Créer un agent simple
agent = Agent(
    model="gemini-2.0-flash",
    name="simple_agent",
    instruction="You are a helpful assistant.",
    description="A simple helpful agent"
)

# Configurer la session
session_service = InMemorySessionService()
session = session_service.create_session(
    app_name="my_app",
    user_id="user123",
    session_id="session001"
)

# Créer le runner
runner = Runner(
    agent=agent,
    app_name="my_app",
    session_service=session_service
)

# Exécuter l'agent
content = types.Content(
    role='user',
    parts=[types.Part(text="Hello!")]
)

events = runner.run(
    user_id="user123",
    session_id="session001",
    new_message=content
)

# Traiter les événements
for event in events:
    if event.is_final_response() and event.content:
        print(event.content.parts[0].text)
```

### Java

```java
import com.google.adk.agents.LlmAgent;
import com.google.adk.runner.InMemoryRunner;
import com.google.adk.sessions.Session;
import com.google.genai.types.Content;
import com.google.genai.types.Part;
import io.reactivex.rxjava3.core.Flowable;
import com.google.adk.events.Event;

// Créer un agent
LlmAgent agent = LlmAgent.builder()
    .model("gemini-2.0-flash")
    .name("simple_agent")
    .description("A simple helpful agent")
    .instruction("You are a helpful assistant.")
    .build();

// Créer le runner
InMemoryRunner runner = new InMemoryRunner(agent, "my_app");

// Créer une session
Session session = runner.sessionService()
    .createSession("my_app", "user123", "session001")
    .blockingGet();

// Exécuter l'agent
Content userMessage = Content.fromParts(
    Part.fromText("Hello!")
);

Flowable<Event> events = runner.runAsync(
    "user123",
    session.id(),
    userMessage
);

// Traiter les événements
events.blockingForEach(event -> {
    if (event.finalResponse()) {
        System.out.println(event.stringifyContent());
    }
});
```

## Agent avec outils

### Définir un outil

```python
from google.adk.tools import FunctionTool

def get_weather(city: str) -> dict:
    """Retrieves the current weather for a city."""
    # Implémentation réelle
    return {
        "status": "success",
        "city": city,
        "temperature": "25°C",
        "condition": "sunny"
    }

weather_tool = FunctionTool(get_weather)
```

### Ajouter l'outil à l'agent

```python
agent = Agent(
    model="gemini-2.0-flash",
    name="weather_agent",
    instruction="You help users get weather information.",
    tools=[weather_tool]
)
```

## Agent Starter Pack

Pour démarrer rapidement avec un projet complet :

```bash
# Installation
pip install agent-starter-pack
# ou
uvx agent-starter-pack create my-agent

# Créer un projet
agent-starter-pack create my-awesome-agent

# Naviguer et démarrer
cd my-awesome-agent
make install
make playground
```

## Validation de l'environnement

### Python

```python
import os
import sys

# Vérifier Python
print(f"Python version: {sys.version}")

# Vérifier l'installation ADK
try:
    import google.adk
    print(f"✅ ADK version: {google.adk.__version__}")
except ImportError:
    print("❌ ADK not installed")

# Vérifier la clé API
api_key = os.getenv('GOOGLE_API_KEY')
if api_key:
    print(f"✅ API key configured: {api_key[:10]}...")
else:
    print("❌ GOOGLE_API_KEY not set")
```

## Structure de projet recommandée

```
my-adk-project/
├── src/
│   └── agent.py          # Définition de l'agent
├── tests/
│   └── test_agent.py     # Tests unitaires
├── requirements.txt      # Dépendances Python
├── .env                  # Variables d'environnement
└── README.md
```

## Prochaines étapes

1. **Ajouter des outils** : Intégrer des APIs externes
2. **Multi-agents** : Créer des workflows avec plusieurs agents
3. **Gestion d'état** : Utiliser les sessions pour la persistance
4. **Déploiement** : Déployer sur Vertex AI ou Cloud Run
5. **Tests** : Écrire des tests pour valider le comportement

## Ressources

- Documentation complète : https://google.github.io/adk-docs/
- Exemples : https://github.com/google/adk-samples
- Agent Starter Pack : https://github.com/GoogleCloudPlatform/agent-starter-pack
