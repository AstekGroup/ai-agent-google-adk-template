# Google ADK Template Repository

[![GitHub](https://img.shields.io/badge/GitHub-AstekGroup-blue)](https://github.com/AstekGroup/ai-agent-google-adk-template)
[![License](https://img.shields.io/badge/License-Educational-yellow)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://www.python.org/)
[![Java](https://img.shields.io/badge/Java-17+-orange)](https://www.oracle.com/java/)

**Date : Novembre 2025**

Ce repository contient des templates complets pour créer des agents Google Agent Development Kit (ADK) en Python et Java, ainsi qu'une documentation exhaustive pour guider les développeurs et les IA.

**Dépôt GitHub :** [https://github.com/AstekGroup/ai-agent-google-adk-template](https://github.com/AstekGroup/ai-agent-google-adk-template)

## 📑 Table des matières

- [🚀 Démarrage rapide](#-démarrage-rapide)
- [📋 Prérequis](#-prérequis)
- [📁 Structure du repository](#-structure-du-repository)
- [💻 Utilisation rapide](#-utilisation-rapide)
- [🎯 Templates disponibles](#-templates-disponibles)
- [⚙️ Configuration](#️-configuration)
- [📚 Documentation](#-documentation)
  - [Règles Cursor](#règles-cursor)
- [🧪 Tests](#-tests)
- [📦 Installation des dépendances](#-installation-des-dépendances)
- [🤝 Contribution](#-contribution)
- [🔗 Ressources externes](#-ressources-externes)

## 🚀 Démarrage rapide

```bash
# Cloner le dépôt
git clone https://github.com/AstekGroup/ai-agent-google-adk-template.git
cd ai-agent-google-adk-template

# Ou via SSH
git clone git@github.com:AstekGroup/ai-agent-google-adk-template.git
```

## 📋 Prérequis

### Pour les templates Python

- **Python** : Version 3.11 ou supérieure
- **Gestionnaire de paquets** : Poetry ou uv (recommandé)
- **Google ADK** : Version 1.3.0 ou supérieure
- **Compte Google Cloud** : Pour utiliser Vertex AI ou AI Studio

### Pour les templates Java

- **Java** : Version 17 ou supérieure (JDK)
- **Maven** : Version 3.8.0 ou supérieure
- **Google ADK** : Version 1.3.0 ou supérieure
- **Compte Google Cloud** : Pour utiliser Vertex AI ou AI Studio

### Configuration Google Cloud

Vous aurez besoin de :
- Un projet Google Cloud avec Vertex AI activé (pour la production)
- OU une clé API Google AI Studio (pour le développement)

## 📁 Structure du repository

```
.
├── .cursor/                      # Règles Cursor pour IA assistants
│   ├── README.md
│   └── rules/
│       └── google-adk-template.mdc  # Règles complètes pour développement avec ADK
├── .gitignore                    # Fichiers ignorés par Git (Python, Java, IDE, etc.)
├── Agents.md                      # Guide complet pour les IA développant avec ADK
├── README.md                      # Ce fichier - Documentation principale
├── resources/                     # Documentation complète sur Google ADK
│   ├── README.md
│   ├── 01-overview.md
│   ├── 02-architecture.md
│   ├── 03-getting-started.md
│   ├── 04-api-reference.md
│   ├── 05-examples-patterns.md
│   ├── 06-deployment.md
│   ├── 07-tools-integrations.md
│   ├── 08-external-resources.md
│   └── 09-patterns-best-practices.md
└── templates/                     # Templates prêts à l'emploi
    ├── README.md                  # Index des templates
    ├── python/                    # Templates Python
    │   ├── README.md
    │   ├── simple-agent/         # Template agent simple
    │   ├── sequential-agent/     # Pipeline séquentiel
    │   ├── parallel-agent/       # Agents parallèles
    │   ├── loop-agent/           # Boucle d'amélioration
    │   ├── rag-agent/            # Agent avec RAG
    │   └── custom-agent/         # Logique personnalisée
    ├── java/                      # Templates Java
    │   ├── README.md
    │   └── simple-agent/         # Template agent simple
    └── docs/                      # Documentation des templates
        ├── README.md
        └── CREATION_GUIDE.md
```

## Utilisation rapide

### Pour les développeurs

1. **Cloner le dépôt** : Utiliser `git clone` pour récupérer les templates
2. **Consulter la documentation** : Parcourir `resources/` pour comprendre Google ADK
3. **Choisir un template** : Voir `templates/README.md` pour la liste complète
4. **Copier et personnaliser** : Copier un template et l'adapter à vos besoins

### Pour les IA assistants

1. **Lire Agents.md** : Guide complet avec patterns et exemples
2. **Consulter les règles Cursor** : `.cursor/rules/google-adk-template.mdc` pour instructions détaillées
3. **Référencer resources/** : Documentation exhaustive de l'API
4. **Suivre les templates** : Exemples de code fonctionnels dans `templates/`

> **Note** : Si vous utilisez Cursor, les règles dans `.cursor/` sont automatiquement chargées et fournissent un contexte complet à l'IA pour vous aider dans le développement.

## 🎯 Templates disponibles

### Python

- **[simple-agent](templates/python/simple-agent/)** : Agent de base avec un outil (⭐ Débutant)
- **[sequential-agent](templates/python/sequential-agent/)** : Pipeline séquentiel (⭐⭐ Intermédiaire)
- **[parallel-agent](templates/python/parallel-agent/)** : Agents parallèles (⭐⭐ Intermédiaire)
- **[loop-agent](templates/python/loop-agent/)** : Boucle d'amélioration (⭐⭐⭐ Avancé)
- **[rag-agent](templates/python/rag-agent/)** : Agent avec RAG (⭐⭐ Intermédiaire)
- **[custom-agent](templates/python/custom-agent/)** : Logique personnalisée (⭐⭐⭐ Avancé)

### Java

- **[simple-agent](templates/java/simple-agent/)** : Agent de base avec Maven (⭐ Débutant)

> **Note** : Consultez le [README des templates Python](templates/python/README.md) et [Java](templates/java/README.md) pour plus de détails sur chaque template.

## 📚 Documentation

### Pour comprendre Google ADK

1. **[Vue d'ensemble](resources/01-overview.md)** : Introduction au framework
2. **[Architecture](resources/02-architecture.md)** : Concepts fondamentaux
3. **[Guide de démarrage](resources/03-getting-started.md)** : Installation et premiers pas
4. **[API Reference](resources/04-api-reference.md)** : Documentation complète de l'API

### Pour développer

1. **[Agents.md](Agents.md)** : Guide complet pour les IA avec patterns
2. **[Règles Cursor](.cursor/rules/google-adk-template.mdc)** : Instructions complètes pour IA assistants
3. **[Patterns et best practices](resources/09-patterns-best-practices.md)** : Architecture et bonnes pratiques
4. **[Exemples](resources/05-examples-patterns.md)** : Exemples de code détaillés

### Pour déployer

1. **[Déploiement](resources/06-deployment.md)** : Guides Vertex AI et Cloud Run
2. **[Scripts de déploiement](templates/python/simple-agent/deployment/)** : Exemples dans les templates

### Règles Cursor

Ce repository inclut des règles Cursor complètes dans `.cursor/rules/` qui fournissent :

- ✅ **Contexte complet** du repository de templates
- ✅ **Instructions d'utilisation** des templates Python et Java
- ✅ **Patterns Google ADK** : Simple, Sequential, Parallel, Loop, RAG, Custom
- ✅ **Best practices** : Configuration, sécurité, performance
- ✅ **Exemples de code** pour chaque pattern
- ✅ **Checklist de développement** pour créer de nouveaux agents
- ✅ **Commandes fréquentes** : Installation, tests, build, déploiement

**Utilisation** : Les règles sont automatiquement chargées par Cursor et aident l'IA à vous assister dans le développement avec Google ADK.

Pour plus de détails, consultez [.cursor/README.md](.cursor/README.md).

## ⚙️ Configuration

### Variables d'environnement

Chaque template contient un fichier `env.example` qu'il faut copier en `.env` et configurer :

```bash
# Copier le fichier d'exemple
cp env.example .env
```

### Configuration minimale requise

```bash
# Backend LLM (1 pour Vertex AI, 0 pour AI Studio)
GOOGLE_GENAI_USE_VERTEXAI=0

# Configuration AI Studio (développement)
GOOGLE_API_KEY=your-api-key-here

# Configuration Vertex AI (production - optionnel)
# GOOGLE_CLOUD_PROJECT=your-project-id
# GOOGLE_CLOUD_LOCATION=us-central1

# Configuration application
APP_NAME=simple_agent
LOG_LEVEL=INFO
```

> **Important** : Le fichier `.env` est ignoré par Git pour des raisons de sécurité. Ne jamais committer vos clés API.

## 📦 Installation des dépendances

### Pour les templates Python

```bash
# Avec Poetry (recommandé)
cd templates/python/simple-agent/
poetry install

# Avec uv (alternative moderne)
uv sync

# Avec pip (si vous préférez)
pip install -r requirements.txt
```

### Pour les templates Java

```bash
# Avec Maven
cd templates/java/simple-agent/
mvn clean install
```

## 🧪 Tests

### Exécuter les tests Python

```bash
cd templates/python/simple-agent/
poetry run pytest

# Avec couverture
poetry run pytest --cov=src tests/
```

### Exécuter les tests Java

```bash
cd templates/java/simple-agent/
mvn test
```

## Exemple rapide

### Créer un agent simple (Python)

```bash
# 1. Copier le template
cp -r templates/python/simple-agent/ my-agent/
cd my-agent

# 2. Installer les dépendances
poetry install

# 3. Configurer les variables d'environnement
cp env.example .env
# Éditer .env avec vos valeurs (GOOGLE_API_KEY)

# 4. Exécuter les tests
poetry run pytest

# 5. Utiliser l'agent
python -c "from src.simple_agent.agent import root_agent; print(root_agent)"
```

### Créer un agent simple (Java)

```bash
# 1. Copier le template
cp -r templates/java/simple-agent/ my-agent/
cd my-agent

# 2. Compiler et tester
mvn clean install

# 3. Configurer
cp env.example .env
# Éditer .env avec vos valeurs

# 4. Exécuter
mvn exec:java -Dexec.mainClass="com.google.adk.samples.simpleagent.Main"
```

## Contribution

Ce dépôt est maintenu par l'organisation **AstekGroup**. Pour contribuer :

### Processus de contribution

1. **Forker le dépôt** ou créer une branche depuis `main`
2. **Créer la structure** dans `templates/python/` ou `templates/java/`
3. **Suivre le [Guide de création](templates/docs/CREATION_GUIDE.md)**
4. **Ajouter une entrée** dans `templates/README.md`
5. **Documenter** dans le README du template
6. **Commiter et pousser** vos modifications
7. **Créer une Pull Request** vers la branche `main`

### Standards de code

- Suivre les conventions de nommage Python/Java
- Documenter le code avec des docstrings
- Ajouter des tests unitaires pour chaque template
- Maintenir la cohérence avec les templates existants

### Structure Git

- **Branche principale** : `main`
- **Commits** : Utiliser des messages clairs et descriptifs
- **Fichiers ignorés** : Vérifier `.gitignore` avant de committer

## 🔗 Ressources externes

- [Documentation officielle ADK](https://google.github.io/adk-docs/)
- [Exemples Google](https://github.com/google/adk-samples)
- [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)

## 📋 Informations du dépôt

- **Organisation** : [AstekGroup](https://github.com/AstekGroup)
- **Branche principale** : `main`
- **Dernière mise à jour** : Novembre 2025
- **Statut** : Actif et maintenu

## 📝 Licence

Ces templates sont fournis à des fins éducatives et de développement. Consultez les licences des projets Google ADK pour plus d'informations.

## 🤝 Support

Pour toute question ou problème :
- Ouvrir une [Issue](https://github.com/AstekGroup/ai-agent-google-adk-template/issues) sur GitHub
- Consulter la [documentation](resources/) dans le dépôt
- Référencer le [Guide Agents.md](Agents.md) pour les IA assistants
