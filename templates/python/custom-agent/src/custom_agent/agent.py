"""Agent personnalisé avec logique d'orchestration avancée."""

from google.adk.agents import BaseAgent, LlmAgent, LoopAgent, SequentialAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from typing import AsyncGenerator
from typing_extensions import override
from .sub_agents import story_generator, critic, reviser, grammar_check, tone_check


class StoryFlowAgent(BaseAgent):
    """
    Agent personnalisé pour génération d'histoires avec logique conditionnelle.
    
    Workflow:
    1. Génération initiale
    2. Boucle critique/refinement
    3. Vérification grammaire et ton
    4. Régénération conditionnelle si ton négatif
    """
    
    def __init__(
        self,
        name: str,
        story_generator: LlmAgent,
        critic: LlmAgent,
        reviser: LlmAgent,
        grammar_check: LlmAgent,
        tone_check: LlmAgent,
    ):
        # Créer la boucle critique/revision
        loop_agent = LoopAgent(
            name="CriticReviserLoop",
            sub_agents=[critic, reviser],
            max_iterations=2
        )
        
        # Créer le séquentiel post-traitement
        sequential_agent = SequentialAgent(
            name="PostProcessing",
            sub_agents=[grammar_check, tone_check]
        )
        
        super().__init__(
            name=name,
            description="Agent personnalisé pour génération d'histoires avec workflow conditionnel",
            sub_agents=[story_generator, loop_agent, sequential_agent]
        )
        
        # Stocker les références avec préfixe _ pour éviter les problèmes Pydantic
        object.__setattr__(self, '_story_generator', story_generator)
        object.__setattr__(self, '_loop_agent', loop_agent)
        object.__setattr__(self, '_sequential_agent', sequential_agent)

    @override
    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        """Logique d'orchestration personnalisée."""
        
        # Étape 1 : Génération initiale
        async for event in self._story_generator.run_async(ctx):
            yield event
        
        if "current_story" not in ctx.session.state:
            return
        
        # Étape 2 : Boucle critique/revision
        async for event in self._loop_agent.run_async(ctx):
            yield event
        
        # Étape 3 : Vérification grammaire et ton
        async for event in self._sequential_agent.run_async(ctx):
            yield event
        
        # Étape 4 : Régénération conditionnelle si ton négatif
        tone_result = ctx.session.state.get("tone_check_result")
        
        if tone_result == "negative":
            # Régénérer l'histoire si le ton est négatif
            async for event in self._story_generator.run_async(ctx):
                yield event


# Créer l'instance de l'agent personnalisé
root_agent = StoryFlowAgent(
    name="StoryFlowAgent",
    story_generator=story_generator,
    critic=critic,
    reviser=reviser,
    grammar_check=grammar_check,
    tone_check=tone_check
)
