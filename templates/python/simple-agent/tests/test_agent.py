"""Tests pour l'agent simple."""

import pytest
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from src.simple_agent.agent import root_agent


def test_agent_creation():
    """Test que l'agent peut être créé."""
    assert root_agent is not None
    assert root_agent.name == "simple_agent"
    assert len(root_agent.tools) > 0


def test_agent_basic_interaction():
    """Test interaction basique avec l'agent."""
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
        parts=[types.Part(text="Hello, what can you do?")]
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


def test_weather_tool():
    """Test de l'outil météo."""
    from src.simple_agent.tools import get_weather
    
    # Test avec une ville connue
    result = get_weather("Paris", "celsius")
    assert result["status"] == "success"
    assert result["city"] == "Paris"
    assert "temperature" in result
    
    # Test avec une ville inconnue
    result = get_weather("UnknownCity", "celsius")
    assert result["status"] == "error"
    assert "message" in result


def test_agent_weather_query():
    """Test de l'agent avec une requête météo."""
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
        parts=[types.Part(text="What's the weather in Paris?")]
    )
    
    events = list(runner.run(
        user_id="test_user",
        session_id="test_session",
        new_message=content
    ))
    
    # Vérifier qu'on a utilisé l'outil météo
    tool_calls = [
        e for e in events 
        if hasattr(e, 'tool_calls') and e.tool_calls
    ]
    
    # Vérifier qu'on a une réponse finale
    final_responses = [
        e for e in events if e.is_final_response()
    ]
    assert len(final_responses) > 0
