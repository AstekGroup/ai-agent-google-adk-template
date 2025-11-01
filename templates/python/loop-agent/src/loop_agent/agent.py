"""Pipeline avec boucle d'amélioration : Initial → [Critic → Refiner]×N."""

from google.adk.agents import Agent, LoopAgent, SequentialAgent
from .sub_agents import initial_writer, critic_agent, refiner_agent

# Créer la boucle de refinement
refinement_loop = LoopAgent(
    name="refinement_loop",
    description="Boucle d'amélioration itérative du contenu",
    sub_agents=[critic_agent, refiner_agent],
    max_iterations=5
)

# Pipeline complet : Initial + Boucle
root_agent = SequentialAgent(
    name="iterative_writing_pipeline",
    description="Génération initiale suivie d'amélioration itérative",
    sub_agents=[initial_writer, refinement_loop]
)
