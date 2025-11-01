"""Agents pour la boucle d'amélioration."""

from google.adk.agents import Agent
from google.adk.tools import ToolContext, FunctionTool

# Fonction pour sortir de la boucle
def exit_loop(tool_context: ToolContext) -> dict:
    """Sortir de la boucle."""
    tool_context.actions.escalate = True
    return {}

# Agent initial : Génère le premier draft
initial_writer = Agent(
    model="gemini-2.5-flash",
    name="initial_writer",
    description="Génère le premier draft du contenu",
    instruction="""You are a creative writer.

Your task:
1. Read the topic from session state key 'topic'
2. Write the first draft of a short story (2-4 sentences)
3. Output only the story text, no introductions or explanations

Be creative and engaging.""",
    output_key="current_document"
)

# Agent critique : Examine le contenu
critic_agent = Agent(
    model="gemini-2.5-flash",
    name="critic",
    description="Critique le contenu actuel",
    instruction="""You are a constructive critic reviewing a short document.

Current document:
```
{current_document}
```

Your task:
1. Review the document for clarity, engagement, and coherence
2. IF you identify 1-2 clear and actionable improvements, provide specific suggestions
3. ELSE IF the document is coherent and addresses the topic adequately, respond exactly: "No major issues found."

Output only the critique OR the exact completion phrase.""",
    output_key="criticism"
)

# Agent refiner : Améliore le contenu ou sort de la boucle
refiner_agent = Agent(
    model="gemini-2.5-flash",
    name="refiner",
    description="Refine le contenu ou sort de la boucle si satisfait",
    instruction="""You are a creative writer refining a document.

Current document:
```
{current_document}
```

Critique:
{criticism}

Your task:
1. IF the critique is exactly "No major issues found.":
   - Call the 'exit_loop' function
   - Do not output any text
2. ELSE:
   - Apply the suggestions to improve the document
   - Output only the refined document text""",
    tools=[FunctionTool(exit_loop)],
    output_key="current_document"
)
