"""Pipeline parallèle : Recherche parallèle → Fusion."""

from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from .sub_agents import (
    researcher_1,
    researcher_2,
    researcher_3,
    merger_agent
)

# Créer le groupe de recherche parallèle
parallel_research = ParallelAgent(
    name="parallel_research",
    description="Exécute plusieurs recherches en parallèle",
    sub_agents=[researcher_1, researcher_2, researcher_3]
)

# Pipeline : Recherche parallèle puis fusion
root_agent = SequentialAgent(
    name="research_and_synthesis",
    description="Recherche parallèle suivie de synthèse",
    sub_agents=[parallel_research, merger_agent]
)
