# Outils et intégrations Google ADK

## Outils intégrés

### GoogleSearchTool

Recherche Google intégrée.

```python
from google.adk.tools import GoogleSearchTool

agent = Agent(
    ...,
    tools=[GoogleSearchTool()]
)
```

### Vertex AI RAG Retrieval

Récupération depuis un corpus RAG.

```python
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag

rag_tool = VertexAiRagRetrieval(
    name='retrieve_docs',
    description='Retrieve documentation from RAG corpus',
    rag_resources=[
        rag.RagResource(rag_corpus="projects/123/locations/us-central1/ragCorpora/456")
    ],
    similarity_top_k=10,
    vector_distance_threshold=0.6,
)

agent = Agent(..., tools=[rag_tool])
```

### Load Memory Tool

Charger depuis la mémoire de l'agent.

```python
from google.adk.tools import load_memory

agent = Agent(
    ...,
    tools=[load_memory]
)
```

### Load Artifacts Tool

Charger des artefacts précédents.

```python
from google.adk.tools import load_artifacts

agent = Agent(
    ...,
    tools=[load_artifacts]
)
```

## Création d'outils personnalisés

### FunctionTool basique

```python
from google.adk.tools import FunctionTool

def get_weather(city: str) -> dict:
    """Retrieves the current weather for a city."""
    return {
        "status": "success",
        "city": city,
        "temperature": "25°C",
        "condition": "sunny"
    }

weather_tool = FunctionTool(get_weather)
```

### Outil asynchrone

```python
import asyncio
from google.adk.tools import FunctionTool

async def async_api_call(endpoint: str) -> dict:
    """Make async API call."""
    await asyncio.sleep(0.5)
    return {"status": "success", "data": {}}

async_tool = FunctionTool(async_api_call)
```

### Outil avec gestion d'erreurs

```python
from google.adk.tools import FunctionTool
import requests

def resilient_api_call(endpoint: str, max_retries: int = 3) -> dict:
    """API call with retry logic."""
    for attempt in range(max_retries):
        try:
            response = requests.get(endpoint, timeout=10)
            response.raise_for_status()
            return {"status": "success", "data": response.json()}
        except Exception as e:
            if attempt == max_retries - 1:
                return {"status": "error", "message": str(e)}
            time.sleep(2 ** attempt)

tool = FunctionTool(resilient_api_call)
```

## Intégrations tierces

### LangChain Tools

```python
from langchain.tools import Tool
from google.adk.tools.langchain_tool import LangChainTool

langchain_tool = Tool(
    name="search",
    func=lambda x: f"Search results for {x}",
    description="Search the web"
)

adk_tool = LangChainTool(langchain_tool)
agent = Agent(..., tools=[adk_tool])
```

### CrewAI Tools

```python
from crewai_tools import SerperDevTool
from google.adk.tools.crewai_tool import CrewaiTool

serper_tool = SerperDevTool(
    n_results=10,
    search_type="news"
)

adk_tool = CrewaiTool(
    name="InternetNewsSearch",
    description="Searches for news articles",
    tool=serper_tool
)

agent = Agent(..., tools=[adk_tool])
```

### OpenAPI Specifications

```python
from google.adk.tools.openapi_tool import OpenApiTool

openapi_tool = OpenApiTool(
    name="api_tool",
    openapi_spec="https://api.example.com/openapi.json",
    base_url="https://api.example.com"
)

agent = Agent(..., tools=[openapi_tool])
```

## Intégration BigQuery

```python
from google.cloud import bigquery
from google.adk.tools import FunctionTool

def query_bigquery(query: str) -> dict:
    """Execute SQL query against BigQuery."""
    client = bigquery.Client()
    query_job = client.query(query)
    results = query_job.result()
    
    rows = [dict(row) for row in results]
    return {
        "status": "success",
        "row_count": len(rows),
        "data": rows
    }

bq_tool = FunctionTool(query_bigquery)
agent = Agent(..., tools=[bq_tool])
```

## Intégration avec bases de données

### PostgreSQL

```python
import psycopg2
from google.adk.tools import FunctionTool

def query_postgres(query: str) -> dict:
    """Execute SQL query against PostgreSQL."""
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    
    return {"status": "success", "data": results}

db_tool = FunctionTool(query_postgres)
```

## Intégration APIs externes

### REST API générique

```python
import requests
from google.adk.tools import FunctionTool

def call_rest_api(
    method: str,
    url: str,
    headers: dict = None,
    body: dict = None
) -> dict:
    """Call a REST API endpoint."""
    response = requests.request(
        method=method,
        url=url,
        headers=headers or {},
        json=body
    )
    return {
        "status": "success" if response.status_code == 200 else "error",
        "status_code": response.status_code,
        "data": response.json()
    }

api_tool = FunctionTool(call_rest_api)
```

### GitHub API

```python
import requests
from google.adk.tools import FunctionTool

def get_github_repo_info(owner: str, repo: str) -> dict:
    """Get information about a GitHub repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
    response = requests.get(url, headers=headers)
    return response.json()

github_tool = FunctionTool(get_github_repo_info)
```

## Intégration LLMs externes

### Via LiteLLM

```python
from google.adk.models.lite_llm import LiteLlm

# OpenAI
agent_openai = Agent(
    model=LiteLlm(model="openai/gpt-4o"),
    ...
)

# Anthropic Claude
agent_claude = Agent(
    model=LiteLlm(model="anthropic/claude-3-haiku-20240307"),
    ...
)

# Cohere
agent_cohere = Agent(
    model=LiteLlm(model="cohere/command"),
    ...
)
```

## Intégration MCP (Model Context Protocol)

```python
from google.adk.tools.mcp_tool import McpTool

mcp_tool = McpTool(
    name="mcp_tool",
    server_url="http://localhost:8000",
    tools=["tool1", "tool2"]
)

agent = Agent(..., tools=[mcp_tool])
```

## Outils de fichiers

### Lecture de fichiers

```python
from google.adk.tools import FunctionTool

def read_file(file_path: str) -> dict:
    """Read content from a file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return {"status": "success", "content": content}
    except Exception as e:
        return {"status": "error", "message": str(e)}

file_tool = FunctionTool(read_file)
```

### Écriture de fichiers

```python
def write_file(file_path: str, content: str) -> dict:
    """Write content to a file."""
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return {"status": "success", "file_path": file_path}
    except Exception as e:
        return {"status": "error", "message": str(e)}

write_tool = FunctionTool(write_file)
```

## Intégration email

```python
import smtplib
from email.mime.text import MIMEText
from google.adk.tools import FunctionTool

def send_email(
    recipient: str,
    subject: str,
    body: str
) -> dict:
    """Send email notification."""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = os.getenv("EMAIL_FROM")
    msg['To'] = recipient
    
    server = smtplib.SMTP(os.getenv("SMTP_HOST"), 587)
    server.starttls()
    server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
    server.send_message(msg)
    server.quit()
    
    return {"status": "success", "recipient": recipient}

email_tool = FunctionTool(send_email)
```

## Patterns d'intégration

### Multi-tool agent

```python
agent = Agent(
    name="multi_tool_agent",
    model="gemini-2.5-flash",
    instruction="Use available tools to help users.",
    tools=[
        weather_tool,
        search_tool,
        file_tool,
        email_tool
    ]
)
```

### Tool avec validation

```python
from pydantic import BaseModel, validator

class WeatherInput(BaseModel):
    city: str
    
    @validator('city')
    def validate_city(cls, v):
        if not v:
            raise ValueError('City cannot be empty')
        return v.lower()

def get_weather(city: WeatherInput) -> dict:
    """Get weather with validation."""
    # Implementation
    pass

tool = FunctionTool(get_weather)
```
