"""Tests pour la boucle d'amélioration."""

import pytest
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from src.loop_agent.agent import root_agent


def test_loop_creation():
    """Test que la boucle peut être créée."""
    assert root_agent is not None
    assert root_agent.name == "iterative_writing_pipeline"


def test_loop_execution():
    """Test exécution de la boucle."""
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name="test_app",
        session_service=session_service
    )
    
    session = session_service.create_session(
        app_name="test_app",
        user_id="test_user",
        session_id="test_session",
        state={"topic": "A robot learning to paint"}
    )
    
    content = types.Content(
        role='user',
        parts=[types.Part(text="Generate and refine a story")]
    )
    
    events = list(runner.run(
        user_id="test_user",
        session_id="test_session",
        new_message=content
    ))
    
    assert len(events) > 0
    
    final_responses = [
        e for e in events if e.is_final_response()
    ]
    assert len(final_responses) > 0
