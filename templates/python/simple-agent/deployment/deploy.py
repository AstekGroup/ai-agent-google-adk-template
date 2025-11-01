"""Script de déploiement pour Vertex AI Agent Engine."""

import os
import sys
from pathlib import Path
from vertexai import agent_engines
from google.cloud import aiplatform

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

def deploy():
    """Déployer l'agent sur Vertex AI Agent Engine."""
    # Vérifier les variables d'environnement
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    location = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
    
    if not project_id:
        raise ValueError("GOOGLE_CLOUD_PROJECT must be set")
    
    # Initialiser Vertex AI
    aiplatform.init(project=project_id, location=location)
    
    # Chemin vers le wheel package
    wheel_path = Path(__file__).parent / "simple_agent-1.0.0-py3-none-any.whl"
    
    if not wheel_path.exists():
        print("Building wheel package...")
        print("Run: poetry build --format=wheel --out-dir deployment")
        print("or: uv build --wheel --out-dir deployment")
        return
    
    # Créer le reasoning engine
    print(f"Deploying agent to Vertex AI Agent Engine...")
    print(f"Project: {project_id}")
    print(f"Location: {location}")
    
    reasoning_engine = agent_engines.ReasoningEngine.create(
        reasoning_engine={
            "display_name": "simple-agent",
            "model_config": {
                "model": "gemini-2.5-flash",
            },
            "source": {
                "package_path": str(wheel_path),
                "entrypoint": "simple_agent.agent:root_agent",
            },
        }
    )
    
    print(f"\n✅ Agent deployed successfully!")
    print(f"Resource ID: {reasoning_engine.resource_name}")
    print(f"\nTo test:")
    print(f"export RESOURCE_ID={reasoning_engine.resource_name}")
    print(f"python test_deployment.py --resource_id=$RESOURCE_ID")


if __name__ == "__main__":
    deploy()
