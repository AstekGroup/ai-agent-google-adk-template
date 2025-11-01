"""Tests pour l'agent RAG."""

import pytest
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import os


def test_rag_agent_creation():
    """Test que l'agent RAG peut être créé."""
    # Skip si RAG_CORPUS n'est pas configuré
    if not os.getenv("RAG_CORPUS"):
        pytest.skip("RAG_CORPUS not configured")
    
    from src.rag_agent.agent import root_agent
    
    assert root_agent is not None
    assert root_agent.name == "rag_agent"
    assert len(root_agent.tools) > 0


def test_rag_query():
    """Test requête RAG."""
    if not os.getenv("RAG_CORPUS"):
        pytest.skip("RAG_CORPUS not configured")
    
    from src.rag_agent.agent import root_agent
    
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
        parts=[types.Part(text="What information is available?")]
    )
    
    events = list(runner.run(
        user_id="test_user",
        session_id="test_session",
        new_message=content
    ))
    
    assert len(events) > 0
