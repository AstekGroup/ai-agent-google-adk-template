"""Configuration pytest pour charger les variables d'environnement."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Charger le fichier .env depuis le répertoire racine du projet
env_path = Path(__file__).parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)
else:
    # Si .env n'existe pas, charger depuis env.example pour les tests
    env_example_path = Path(__file__).parent.parent / 'env.example'
    if env_example_path.exists():
        load_dotenv(env_example_path)

