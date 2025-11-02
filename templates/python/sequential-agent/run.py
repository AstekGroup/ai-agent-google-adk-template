#!/usr/bin/env python3
"""Script pour lancer l'agent séquentiel de manière interactive."""

import asyncio
from pathlib import Path
from dotenv import load_dotenv
from src.sequential_agent.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Charger le fichier .env
env_path = Path(__file__).parent / '.env'
if env_path.exists():
    load_dotenv(env_path)
else:
    print("⚠️  Avertissement: fichier .env introuvable. Assurez-vous qu'il existe et contient GOOGLE_API_KEY")


async def main():
    """Fonction principale pour lancer l'agent."""
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name="agents",
        session_service=session_service
    )
    
    # Créer une session
    session = await session_service.create_session(
        app_name="agents",
        user_id="user123",
        session_id="session001"
    )
    
    print("🤖 Agent Séquentiel (Pipeline d'écriture) démarré!")
    print("💡 Tapez 'quit' ou 'exit' pour quitter\n")
    
    while True:
        try:
            # Demander une question à l'utilisateur
            user_input = input("Vous: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Au revoir!")
                break
            
            if not user_input:
                continue
            
            # Créer le message
            content = types.Content(
                role='user',
                parts=[types.Part(text=user_input)]
            )
            
            # Exécuter l'agent
            print("\n🤔 Traitement en cours (Writer → Reviewer → Refiner)...\n")
            events = []
            async for event in runner.run_async(
                user_id="user123",
                session_id="session001",
                new_message=content
            ):
                events.append(event)
            
            # Afficher la réponse finale
            final_responses = [
                e for e in events if e.is_final_response() and e.content
            ]
            
            if final_responses:
                for response in final_responses:
                    if response.content and response.content.parts:
                        print(f"Agent: {response.content.parts[0].text}\n")
            else:
                print("Agent: (Pas de réponse finale)\n")
                
        except KeyboardInterrupt:
            print("\n\n👋 Au revoir!")
            break
        except Exception as e:
            print(f"\n❌ Erreur: {e}\n")


if __name__ == "__main__":
    asyncio.run(main())

