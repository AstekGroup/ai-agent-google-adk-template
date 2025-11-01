"""Tests pour l'agent personnalisé."""

import pytest
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from src.custom_agent.agent import root_agent


def test_custom_agent_creation():
    """Test que l'agent personnalisé peut être créé."""
    assert root_agent is not None
    assert root_agent.name == "StoryFlowAgent"
    assert isinstance(root_agent, type(root_agent).__bases__[0])


@pytest.mark.asyncio
async def test_custom_agent_execution():
    """Test exécution de l'agent personnalisé."""
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name="agents",
        session_service=session_service
    )
    
    session = await session_service.create_session(
        app_name="agents",
        user_id="test_user",
        session_id="test_session",
        state={"topic": "A robot learning to paint"}
    )
    
    content = types.Content(
        role='user',
        parts=[types.Part(text="Generate a story")]
    )
    
    events = []
    async for event in runner.run_async(
        user_id="test_user",
        session_id="test_session",
        new_message=content
    ):
        events.append(event)
    
    assert len(events) > 0
    
    final_responses = [
        e for e in events if e.is_final_response()
    ]
    assert len(final_responses) > 0
