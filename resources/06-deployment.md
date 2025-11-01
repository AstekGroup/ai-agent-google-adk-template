# Déploiement Google ADK

## Déploiement local

### Exécution en développement

```bash
# Avec Python
python agent.py

# Avec uvicorn (pour serveur FastAPI)
uvicorn app.server:app --host 0.0.0.0 --port 8000 --reload
```

### Variables d'environnement locales

```bash
# .env file
GOOGLE_API_KEY=your-api-key
GOOGLE_GENAI_USE_VERTEXAI=False
APP_NAME=my_app
```

## Déploiement sur Vertex AI Agent Engine

### Prérequis

```bash
# Authentification
gcloud auth application-default login
gcloud auth application-default set-quota-project $GOOGLE_CLOUD_PROJECT

# Variables d'environnement
export GOOGLE_GENAI_USE_VERTEXAI="True"
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"
```

### Préparation du package

```bash
# Avec Poetry
poetry build --format=wheel --out-dir deployment

# Avec uv
uv build --wheel --out-dir deployment
```

### Configuration des permissions

```bash
export RE_SA="service-${GOOGLE_CLOUD_PROJECT_NUMBER}@gcp-sa-aiplatform-re.iam.gserviceaccount.com"

gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
    --member="serviceAccount:${RE_SA}" \
    --role="roles/bigquery.user"
```

### Déploiement

```python
# deployment/deploy.py
import os
from vertexai import agent_engines
from google.cloud import aiplatform

aiplatform.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION")
)

# Créer le reasoning engine
reasoning_engine = agent_engines.ReasoningEngine.create(
    reasoning_engine={
        "display_name": "my-agent",
        "model_config": {
            "model": "gemini-2.5-flash",
        },
        "source": {
            "package_path": "deployment/my_agent-1.0.0-py3-none-any.whl",
            "entrypoint": "agent_code.agent:root_agent",
        },
    }
)

print(f"Deployed: {reasoning_engine.resource_name}")
```

### Test du déploiement

```python
# deployment/test_deployment.py
import os
from vertexai import agent_engines

RESOURCE_ID = os.getenv("RESOURCE_ID")
USER_ID = "test_user"

remote_agent = agent_engines.get(RESOURCE_ID)
session = remote_agent.create_session(user_id=USER_ID)

# Stream responses
for event in remote_agent.stream_query(
    user_id=USER_ID,
    session_id=session["id"],
    message="Hello!",
):
    parts = event.get("content", {}).get("parts", [])
    for part in parts:
        if "text" in part:
            print(part["text"], end="", flush=True)
```

### Suppression

```python
# deployment/deploy.py --delete
agent_engines.delete(reasoning_engine_id=RESOURCE_ID)
```

## Déploiement sur Cloud Run

### Dockerfile

```dockerfile
FROM python:3.11-slim

RUN pip install --no-cache-dir uv==0.6.12

WORKDIR /code

COPY ./pyproject.toml ./README.md ./uv.lock* ./
COPY ./app ./app

RUN uv sync --frozen

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Déploiement

```bash
# Build et push
gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/my-agent

# Déployer
gcloud run deploy my-agent \
    --image gcr.io/$GOOGLE_CLOUD_PROJECT/my-agent \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT,GOOGLE_CLOUD_LOCATION=us-central1
```

### Serveur FastAPI

```python
# app/server.py
from fastapi import FastAPI
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent_code.agent import root_agent

app = FastAPI()
session_service = InMemorySessionService()

@app.post("/query")
async def query(user_id: str, session_id: str, message: str):
    runner = Runner(
        agent=root_agent,
        app_name="my_app",
        session_service=session_service
    )
    
    content = types.Content(
        role='user',
        parts=[types.Part(text=message)]
    )
    
    events = runner.run(user_id=user_id, session_id=session_id, new_message=content)
    
    responses = []
    for event in events:
        if event.is_final_response() and event.content:
            responses.append(event.content.parts[0].text)
    
    return {"response": " ".join(responses)}
```

## CI/CD avec Agent Starter Pack

### Configuration CI/CD

```bash
# Installation
uvx agent-starter-pack setup-cicd

# Avec options
uvx agent-starter-pack setup-cicd \
    --staging-project your-staging-project \
    --prod-project your-prod-project \
    --repository-name my-agent \
    --repository-owner your-username \
    --auto-approve
```

### Workflow GitHub Actions

```yaml
# .github/workflows/deploy.yml
name: Deploy Agent

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: google-github-actions/setup-gcloud@v1
      - name: Deploy to Cloud Run
        run: |
          gcloud run deploy my-agent --source .
```

## Monitoring et observabilité

### Intégration avec AgentOps

```python
from agentops import AgentOps

agentops = AgentOps(api_key="your-api-key")
agentops.start_session()

# Dans votre agent
agent = Agent(
    ...,
    observability_provider=agentops
)
```

### Logging personnalisé

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_callback(ctx: CallbackContext):
    logger.info(f"Agent {ctx.agent.name} executing")
    logger.info(f"Session: {ctx.session.id}")

agent = Agent(
    ...,
    before_agent_callback=log_callback
)
```

## Variables d'environnement de production

```bash
# Vertex AI
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1

# Ou AI Studio (développement uniquement)
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=your-api-key

# Application
APP_NAME=my_app
LOG_LEVEL=INFO
```

## Scaling

### Vertex AI Agent Engine

- Scaling automatique géré par Google Cloud
- Pas de configuration supplémentaire nécessaire

### Cloud Run

```bash
# Configuration de scaling
gcloud run services update my-agent \
    --min-instances=1 \
    --max-instances=10 \
    --concurrency=80 \
    --cpu=2 \
    --memory=4Gi
```

## Sécurité

### Service Account

```bash
# Créer un service account
gcloud iam service-accounts create agent-sa \
    --display-name="Agent Service Account"

# Accorder les permissions
gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
    --member="serviceAccount:agent-sa@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com" \
    --role="roles/aiplatform.user"
```

### Secrets Management

```python
from google.cloud import secretmanager

def get_secret(secret_id: str) -> str:
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{PROJECT_ID}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")
```
