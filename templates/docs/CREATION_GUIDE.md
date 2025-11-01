# Guide de création de templates Google ADK

**Date : Novembre 2025**

Ce guide explique comment créer de nouveaux templates pour Google ADK basés sur les patterns et best practices documentés.

## Structure d'un template

Un template doit contenir :

1. **README.md** : Documentation complète du template
2. **Fichiers de configuration** : pyproject.toml (Python) ou pom.xml (Java)
3. **Code source** : Structure complète avec exemples fonctionnels
4. **Tests** : Tests unitaires de base
5. **Scripts de déploiement** : Configuration pour Vertex AI ou Cloud Run
6. **Variables d'environnement** : .env.example avec documentation

## Checklist de création

### Phase 1 : Planification

- [ ] Définir le cas d'usage du template
- [ ] Identifier les patterns ADK à utiliser
- [ ] Lister les dépendances nécessaires
- [ ] Prévoir la structure de fichiers

### Phase 2 : Structure de base

- [ ] Créer la structure de répertoires
- [ ] Configurer pyproject.toml ou pom.xml
- [ ] Créer .env.example
- [ ] Ajouter .gitignore approprié

### Phase 3 : Code source

- [ ] Implémenter l'agent principal
- [ ] Créer les outils nécessaires
- [ ] Ajouter les callbacks si nécessaire
- [ ] Documenter chaque composant

### Phase 4 : Tests

- [ ] Créer tests unitaires
- [ ] Créer tests d'intégration
- [ ] Vérifier que tous les tests passent

### Phase 5 : Déploiement

- [ ] Créer script de déploiement Vertex AI
- [ ] Créer Dockerfile si Cloud Run
- [ ] Tester le déploiement

### Phase 6 : Documentation

- [ ] README.md complet
- [ ] Commentaires dans le code
- [ ] Exemples d'utilisation
- [ ] Guide de personnalisation

## Template de base Python

### Structure minimale

```
template-name/
├── README.md
├── pyproject.toml
├── .env.example
├── .gitignore
├── src/
│   └── agent_name/
│       ├── __init__.py
│       ├── agent.py
│       └── tools.py
├── tests/
│   ├── __init__.py
│   └── test_agent.py
└── deployment/
    └── deploy.py
```

### pyproject.toml exemple

```toml
[tool.poetry]
name = "agent-name"
version = "1.0.0"
description = "Description du template"
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.11"
google-adk = "^1.3.0"
python-dotenv = "^1.0.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
pytest-asyncio = "^0.21.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### agent.py exemple

```python
"""Agent principal du template."""
from google.adk.agents import Agent
from .tools import get_example_tool

root_agent = Agent(
    model="gemini-2.5-flash",
    name="example_agent",
    description="Description de l'agent pour délégation",
    instruction="""Instructions système claires et précises.
    Décrire le rôle, les capacités, et les limites.""",
    tools=[get_example_tool]
)
```

## Template de base Java

### Structure minimale

```
template-name/
├── README.md
├── pom.xml
├── .env.example
├── .gitignore
└── src/
    └── main/
        ├── java/
        │   └── com/google/adk/samples/agentname/
        │       ├── Agent.java
        │       ├── Main.java
        │       └── tools/
        │           └── ExampleTool.java
        └── resources/
            └── application.properties
```

### pom.xml exemple

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.google.adk.samples</groupId>
    <artifactId>agent-name</artifactId>
    <version>1.0.0</version>

    <properties>
        <java.version>17</java.version>
        <google-adk.version>1.3.0</google-adk.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>com.google.adk</groupId>
            <artifactId>google-adk</artifactId>
            <version>${google-adk.version}</version>
        </dependency>
    </dependencies>
</project>
```

## Patterns à documenter

Pour chaque template, documenter :

1. **Architecture** : Diagramme ou description du flux
2. **Composants** : Liste des agents, outils, callbacks
3. **Cas d'usage** : Quand utiliser ce template
4. **Personnalisation** : Comment adapter pour besoins spécifiques
5. **Extensions** : Idées pour aller plus loin

## Exemples de templates avancés

### Template RAG Agent

```python
from google.adk.agents import Agent
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag

rag_tool = VertexAiRagRetrieval(
    name='retrieve_docs',
    description='Retrieve documentation',
    rag_resources=[rag.RagResource(rag_corpus=os.getenv("RAG_CORPUS"))],
    similarity_top_k=10
)

rag_agent = Agent(
    model='gemini-2.5-flash',
    name='rag_agent',
    instruction="""You are a documentation assistant.
    Use RAG retrieval to find relevant information.""",
    tools=[rag_tool]
)
```

### Template Multi-Agent Sequential

```python
from google.adk.agents import Agent, SequentialAgent

writer = Agent(name="writer", ...)
reviewer = Agent(name="reviewer", ...)
refiner = Agent(name="refiner", ...)

pipeline = SequentialAgent(
    name="writing_pipeline",
    sub_agents=[writer, reviewer, refiner]
)
```

## Validation

Avant de considérer un template comme complet :

1. ✅ Code fonctionne sans erreur
2. ✅ Tests passent tous
3. ✅ Documentation complète
4. ✅ Déploiement testé
5. ✅ Exemples d'utilisation fournis
6. ✅ Variables d'environnement documentées

## Ressources

- [Agents.md](../../Agents.md) - Guide pour les IA
- [Documentation ADK](../resources/)
- [Exemples officiels](https://github.com/google/adk-samples)
