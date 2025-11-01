"""Pipeline séquentiel : Writer → Reviewer → Refiner."""

from google.adk.agents import Agent, SequentialAgent
from .sub_agents import writer_agent, reviewer_agent, refiner_agent

# Créer le pipeline séquentiel
root_agent = SequentialAgent(
    name="writing_pipeline",
    description="Pipeline séquentiel pour génération de contenu avec validation",
    sub_agents=[writer_agent, reviewer_agent, refiner_agent]
)
