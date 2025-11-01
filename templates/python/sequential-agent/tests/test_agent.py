"""Tests pour le pipeline séquentiel."""

import pytest
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from src.sequential_agent.agent import root_agent


def test_pipeline_creation():
    """Test que le pipeline peut être créé."""
    assert root_agent is not None
    assert root_agent.name == "writing_pipeline"
    assert len(root_agent.sub_agents) == 3


def test_pipeline_execution():
    """Test exécution complète du pipeline."""
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name="test_app",
        session_service=session_service
    )
    
    session = session_service.create_session(
        app_name="test_app",
        user_id="test_user",
        session_id="test_session"
    )
    
    content = types.Content(
        role='user',
        parts=[types.Part(text="Write a short paragraph about artificial intelligence")]
    )
    
    events = list(runner.run(
        user_id="test_user",
        session_id="test_session",
        new_message=content
    ))
    
    # Vérifier qu'on a reçu des événements
    assert len(events) > 0
    
    # Vérifier qu'on a une réponse finale
    final_responses = [
        e for e in events if e.is_final_response()
    ]
    assert len(final_responses) > 0
    
    # Vérifier que le pipeline a produit du contenu final
    final_session = session_service.get_session(
        app_name="test_app",
        user_id="test_user",
        session_id="test_session"
    )
    
    # Le contenu final devrait être dans l'état
    assert "final_content" in final_session.state or "generated_content" in final_session.state


def test_sub_agents_order():
    """Test que les sous-agents sont dans le bon ordre."""
    sub_agents = root_agent.sub_agents
    assert sub_agents[0].name == "writer"
    assert sub_agents[1].name == "reviewer"
    assert sub_agents[2].name == "refiner"
