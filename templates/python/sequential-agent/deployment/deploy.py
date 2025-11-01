"""Script de déploiement pour Vertex AI Agent Engine."""

import os
import sys
from pathlib import Path
from vertexai import agent_engines
from google.cloud import aiplatform

sys.path.insert(0, str(Path(__file__).parent.parent))

def deploy():
    """Déployer l'agent sur Vertex AI Agent Engine."""
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    location = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
    
    if not project_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT must be set")
    
    aiplatform.init(project=project_id, location=location)
    
    wheel_path = Path(__file__).parent / "sequential_agent-1.0.0-py3-none-any.whl"
    
    if not wheel_path.exists():
        print("Building wheel package...")
        print("Run: poetry build --format=wheel --out-dir deployment")
        return
    
    print(f"Deploying sequential agent pipeline...")
    print(f"Project: {project_id}, Location: {location}")
    
    reasoning_engine = agent_engines.ReasoningEngine.create(
        reasoning_engine={
            "display_name": "sequential-agent",
            "model_config": {"model": "gemini-2.5-flash"},
            "source": {
                "package_path": str(wheel_path),
                "entrypoint": "sequential_agent.agent:root_agent",
            },
        }
    )
    
    print(f"\n✅ Pipeline deployed successfully!")
    print(f"Resource ID: {reasoning_engine.resource_name}")


if __name__ == "__main__":
    deploy()
