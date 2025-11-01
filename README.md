# Google ADK Template Repository

**Date : Novembre 2025**

Ce repository contient des templates complets pour créer des agents Google Agent Development Kit (ADK) en Python et Java, ainsi qu'une documentation exhaustive pour guider les développeurs et les IA.

## Structure du repository

```
.
├── Agents.md                      # Guide complet pour les IA développant avec ADK
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
    │   └── simple-agent/         # Template agent simple
    ├── java/                      # Templates Java
    │   ├── README.md
    │   └── simple-agent/         # Template agent simple
    └── docs/                      # Documentation des templates
        ├── README.md
        └── CREATION_GUIDE.md
```

## Utilisation rapide

### Pour les développeurs

1. **Consulter la documentation** : Parcourir `resources/` pour comprendre Google ADK
2. **Choisir un template** : Voir `templates/README.md` pour la liste
3. **Copier et personnaliser** : Copier un template et l'adapter à vos besoins

### Pour les IA assistants

1. **Lire Agents.md** : Guide complet avec patterns et exemples
2. **Référencer resources/** : Documentation exhaustive de l'API
3. **Suivre les templates** : Exemples de code fonctionnels

## Templates disponibles

### Python

- **simple-agent** : Agent de base avec un outil (⭐ Débutant)
- **sequential-agent** : Pipeline séquentiel (⭐⭐ Intermédiaire)
- **parallel-agent** : Agents parallèles (⭐⭐ Intermédiaire)
- **loop-agent** : Boucle d'amélioration (⭐⭐⭐ Avancé)
- **rag-agent** : Agent avec RAG (⭐⭐ Intermédiaire)
- **custom-agent** : Logique personnalisée (⭐⭐⭐ Avancé)

### Java

- **simple-agent** : Agent de base avec Maven (⭐ Débutant)
- **multi-agent** : Orchestration multi-agents (⭐⭐⭐ Avancé)

## Documentation

### Pour comprendre Google ADK

1. **[Vue d'ensemble](resources/01-overview.md)** : Introduction au framework
2. **[Architecture](resources/02-architecture.md)** : Concepts fondamentaux
3. **[Guide de démarrage](resources/03-getting-started.md)** : Installation et premiers pas
4. **[API Reference](resources/04-api-reference.md)** : Documentation complète de l'API

### Pour développer

1. **[Agents.md](Agents.md)** : Guide complet pour les IA avec patterns
2. **[Patterns et best practices](resources/09-patterns-best-practices.md)** : Architecture et bonnes pratiques
3. **[Exemples](resources/05-examples-patterns.md)** : Exemples de code détaillés

### Pour déployer

1. **[Déploiement](resources/06-deployment.md)** : Guides Vertex AI et Cloud Run
2. **[Scripts de déploiement](templates/python/simple-agent/deployment/)** : Exemples dans les templates

## Exemple rapide

### Créer un agent simple

```bash
# 1. Copier le template
cp -r templates/python/simple-agent/ my-agent/

# 2. Installer les dépendances
cd my-agent
poetry install

# 3. Configurer
cp env.example .env
# Éditer .env avec vos valeurs

# 4. Utiliser
python -c "from src.simple_agent.agent import root_agent; print(root_agent)"
```

## Contribution

Pour ajouter un template :

1. Créer la structure dans `templates/python/` ou `templates/java/`
2. Suivre le [Guide de création](templates/docs/CREATION_GUIDE.md)
3. Ajouter une entrée dans `templates/README.md`
4. Documenter dans le README du template

## Ressources externes

- [Documentation officielle ADK](https://google.github.io/adk-docs/)
- [Exemples Google](https://github.com/google/adk-samples)
- [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)

## Licence

Ces templates sont fournis à des fins éducatives et de développement. Consultez les licences des projets Google ADK pour plus d'informations.
