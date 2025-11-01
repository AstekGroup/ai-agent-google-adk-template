# Exemples et patterns Google ADK

## Exemples de base

### Agent simple avec outil

```python
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

def get_capital_city(country: str) -> str:
    """Retrieves the capital city for a given country."""
    capitals = {"france": "Paris", "japan": "Tokyo", "canada": "Ottawa"}
    return capitals.get(country.lower(), f"Sorry, I don't know the capital of {country}.")

agent = Agent(
    model="gemini-2.0-flash",
    name="capital_agent",
    description="Answers user questions about the capital city of a given country.",
    instruction="""You are an agent that provides the capital city of a country.
When a user asks for the capital of a country:
1. Identify the country name from the user's query.
2. Use the `get_capital_city` tool to find the capital.
3. Respond clearly to the user, stating the capital city.""",
    tools=[get_capital_city]
)

session_service = InMemorySessionService()
session = session_service.create_session(
    app_name="capital_app",
    user_id="user123",
    session_id="session001"
)

runner = Runner(
    agent=agent,
    app_name="capital_app",
    session_service=session_service
)

content = types.Content(role='user', parts=[types.Part(text="What's the capital of France?")])
events = runner.run(user_id="user123", session_id="session001", new_message=content)

for event in events:
    if event.is_final_response() and event.content:
        print(event.content.parts[0].text)
```

## Patterns d'orchestration

### Pipeline séquentiel : Code Writer → Reviewer → Refactorer

```python
from google.adk.agents import Agent, SequentialAgent
from google.adk.runners import InMemoryRunner

code_writer = Agent(
    name="CodeWriterAgent",
    model="gemini-2.0-flash",
    instruction="Write Python code based on user's request. Output only code.",
    output_key="generated_code"
)

code_reviewer = Agent(
    name="CodeReviewerAgent",
    model="gemini-2.0-flash",
    instruction="Review the code: {generated_code}. Provide feedback.",
    output_key="review_comments"
)

code_refactorer = Agent(
    name="CodeRefactorerAgent",
    model="gemini-2.0-flash",
    instruction="Refactor code: {generated_code} based on: {review_comments}",
    output_key="refactored_code"
)

pipeline = SequentialAgent(
    name="CodePipelineAgent",
    sub_agents=[code_writer, code_reviewer, code_refactorer]
)

runner = InMemoryRunner(pipeline, app_name="code_pipeline")
session = runner.session_service().create_session("code_pipeline", "user456").blocking_get()

user_message = types.Content.from_parts(
    types.Part.from_text("Write a function to calculate factorial")
)

for event in runner.run_async("user456", session.id(), user_message):
    if event.final_response():
        print(event.stringify_content())
```

### Recherche parallèle

```python
from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.tools import GoogleSearchTool

researcher_1 = Agent(
    name="RenewableEnergyResearcher",
    model="gemini-2.0-flash",
    instruction="Research renewable energy sources. Summarize findings.",
    tools=[GoogleSearchTool()],
    output_key="renewable_energy_result"
)

researcher_2 = Agent(
    name="EVResearcher",
    model="gemini-2.0-flash",
    instruction="Research electric vehicle technology. Summarize findings.",
    tools=[GoogleSearchTool()],
    output_key="ev_technology_result"
)

researcher_3 = Agent(
    name="CarbonCaptureResearcher",
    model="gemini-2.0-flash",
    instruction="Research carbon capture methods. Summarize findings.",
    tools=[GoogleSearchTool()],
    output_key="carbon_capture_result"
)

parallel_research = ParallelAgent(
    name="ParallelWebResearchAgent",
    sub_agents=[researcher_1, researcher_2, researcher_3]
)

merger = Agent(
    name="SynthesisAgent",
    model="gemini-2.0-flash",
    instruction="""Synthesize these research summaries:
    * Renewable Energy: {renewable_energy_result}
    * Electric Vehicles: {ev_technology_result}
    * Carbon Capture: {carbon_capture_result}
    Output a structured report."""
)

pipeline = SequentialAgent(
    name="ResearchAndSynthesisPipeline",
    sub_agents=[parallel_research, merger]
)
```

### Boucle d'amélioration itérative

```python
from google.adk.agents import Agent, LoopAgent, SequentialAgent
from google.adk.tools import ToolContext

def exit_loop(tool_context: ToolContext):
    """Exit the refinement loop."""
    tool_context.actions.escalate = True
    return {}

initial_writer = Agent(
    name="InitialWriterAgent",
    model="gemini-2.0-flash",
    instruction="Write first draft on topic: {topic}. Output only story text.",
    output_key="current_document"
)

critic = Agent(
    name="CriticAgent",
    model="gemini-2.0-flash",
    instruction="""Review: {current_document}
    IF improvements needed, provide suggestions.
    ELSE respond exactly: 'No major issues found.'""",
    output_key="criticism"
)

refiner = Agent(
    name="RefinerAgent",
    model="gemini-2.0-flash",
    instruction="""Current: {current_document}
    Critique: {criticism}
    IF critique is 'No major issues found.', call exit_loop.
    ELSE refine the document.""",
    tools=[exit_loop],
    output_key="current_document"
)

refinement_loop = LoopAgent(
    name="RefinementLoop",
    sub_agents=[critic, refiner],
    max_iterations=5
)

pipeline = SequentialAgent(
    name="IterativeWritingPipeline",
    sub_agents=[initial_writer, refinement_loop]
)
```

## Patterns multi-agents

### Agent avec sous-agents spécialisés

```python
blog_planner = Agent(
    name="blog_planner",
    model="gemini-2.5-flash",
    instruction="Create detailed blog post outlines.",
)

blog_writer = Agent(
    name="blog_writer",
    model="gemini-2.5-pro",
    instruction="Write engaging technical blog posts.",
)

blog_editor = Agent(
    name="blog_editor",
    model="gemini-2.5-flash",
    instruction="Review and improve blog posts.",
)

main_agent = Agent(
    name="interactive_blogger_agent",
    model="gemini-2.5-flash",
    instruction="""Your workflow:
    1. Plan: Generate outline using blog_planner
    2. Refine: Iterate on outline based on feedback
    3. Write: Create blog post using blog_writer
    4. Edit: Revise using blog_editor
    5. Export: Save final version""",
    sub_agents=[blog_planner, blog_writer, blog_editor]
)
```

## Patterns avec RAG

### Agent avec RAG Vertex AI

```python
from google.adk.agents import Agent
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag
import os

rag_retrieval = VertexAiRagRetrieval(
    name='retrieve_rag_documentation',
    description='Retrieve documentation from RAG corpus',
    rag_resources=[
        rag.RagResource(
            rag_corpus=os.environ.get("RAG_CORPUS")
        )
    ],
    similarity_top_k=10,
    vector_distance_threshold=0.6,
)

rag_agent = Agent(
    model='gemini-2.5-flash',
    name='ask_rag_agent',
    instruction="""You are a documentation assistant. Use the RAG retrieval tool
    to find relevant information and provide accurate answers with proper citations.""",
    tools=[rag_retrieval]
)
```

## Patterns de gestion d'état

### Initialisation de l'état de session

```python
from google.adk.agents.callback_context import CallbackContext

def initialize_session_state(ctx: CallbackContext):
    if "conversation_history" not in ctx.state:
        ctx.state["conversation_history"] = []
    
    if "user_preferences" not in ctx.state:
        ctx.state["user_preferences"] = {
            "risk_tolerance": None,
            "investment_horizon": None
        }

def track_conversation(ctx: CallbackContext):
    current_message = ctx._invocation_context.message
    ctx.state["conversation_history"].append({
        "turn": len(ctx.state["conversation_history"]) + 1,
        "user_message": current_message,
        "timestamp": datetime.now().isoformat()
    })

agent = Agent(
    name="stateful_agent",
    model="gemini-2.5-pro",
    before_agent_callback=initialize_session_state,
    before_turn_callback=track_conversation
)
```

## Patterns avec schémas structurés

### Entrée/sortie structurées

```python
from google.adk.agents import Agent
from pydantic import BaseModel, Field

class CountryInput(BaseModel):
    country: str = Field(description="The country to get information about.")

class CapitalInfoOutput(BaseModel):
    capital: str = Field(description="The capital city.")
    population_estimate: str = Field(description="Estimated population.")

agent = Agent(
    model="gemini-2.0-flash",
    name="structured_info_agent",
    instruction="""Provide country information. Input: JSON with 'country'.
    Output: JSON with 'capital' and 'population_estimate'.""",
    input_schema=CountryInput,
    output_schema=CapitalInfoOutput,
    output_key="structured_info_result"
)

# Utilisation
user_message = types.Content.from_parts(
    types.Part.from_text('{"country": "France"}')
)

# Résultat dans session.state["structured_info_result"]
```

## Patterns avec planification

### Agent avec Built-in Planner

```python
from google.adk import Agent
from google.adk.planners import BuiltInPlanner
from google.genai import types

thinking_config = types.ThinkingConfig(
    include_thoughts=True,
    thinking_budget=256
)

planner = BuiltInPlanner(thinking_config=thinking_config)

agent = Agent(
    model="gemini-2.5-flash",
    name="weather_and_time_agent",
    instruction="You return time and weather information.",
    planner=planner,
    tools=[get_weather, get_current_time]
)
```

## Patterns A2A

### Exposer un agent

```python
from google.adk import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a

def roll_die(sides: int) -> int:
    """Roll a die."""
    import random
    return random.randint(1, sides)

agent = Agent(
    model='gemini-2.0-flash',
    name='hello_world_agent',
    instruction="I roll dice and answer questions.",
    tools=[roll_die]
)

a2a_app = to_a2a(agent, port=8001)
# Démarrer : uvicorn module.path:a2a_app --host localhost --port 8001
```

### Consommer un agent distant

```python
from google.adk.a2a import RemoteA2aAgent

remote_agent = RemoteA2aAgent(
    name="remote_prime_checker",
    agent_card_url="http://localhost:8001/.well-known/agent-card.json"
)

root_agent = Agent(
    model='gemini-2.0-flash',
    name='root_agent',
    instruction="Use remote_prime_checker for prime number checks.",
    tools=[remote_agent]
)
```

## Patterns de gestion d'erreurs

### Outil avec retry

```python
from google.adk.tools import FunctionTool
import time

def resilient_api_call(endpoint: str, max_retries: int = 3) -> dict:
    """Make API call with retry logic."""
    for attempt in range(max_retries):
        try:
            response = requests.get(endpoint, timeout=10)
            response.raise_for_status()
            return {"status": "success", "data": response.json()}
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                return {"status": "error", "message": str(e)}
            time.sleep(2 ** attempt)  # Exponential backoff

agent = Agent(
    name="resilient_agent",
    model="gemini-2.5-flash",
    tools=[FunctionTool(resilient_api_call)]
)
```
