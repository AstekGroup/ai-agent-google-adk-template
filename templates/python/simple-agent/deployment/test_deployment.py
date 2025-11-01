"""Script de test pour agent déployé."""

import argparse
import os
from vertexai import agent_engines


def test_deployment(resource_id: str, user_id: str = "test_user"):
    """Tester l'agent déployé."""
    remote_agent = agent_engines.get(resource_id)
    
    # Créer une session
    session = remote_agent.create_session(user_id=user_id)
    print(f"Session created: {session['id']}")
    
    # Tester une requête simple
    print("\nTesting agent with query: 'What's the weather in Paris?'")
    
    for event in remote_agent.stream_query(
        user_id=user_id,
        session_id=session["id"],
        message="What's the weather in Paris?",
    ):
        parts = event.get("content", {}).get("parts", [])
        for part in parts:
            if "text" in part:
                print(part["text"], end="", flush=True)
    
    print("\n\n✅ Test completed successfully!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test deployed agent")
    parser.add_argument(
        "--resource_id",
        required=True,
        help="Resource ID of the deployed agent"
    )
    parser.add_argument(
        "--user_id",
        default="test_user",
        help="User ID for testing"
    )
    
    args = parser.parse_args()
    test_deployment(args.resource_id, args.user_id)
