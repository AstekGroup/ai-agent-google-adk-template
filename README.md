# Google ADK Template Repository

[![GitHub](https://img.shields.io/badge/GitHub-AstekGroup-blue)](https://github.com/AstekGroup/ai-agent-google-adk-template)
[![License](https://img.shields.io/badge/License-Educational-yellow)](LICENSE)

**Date : Novembre 2025**

Ce repository contient des templates complets pour créer des agents Google Agent Development Kit (ADK) en Python et Java, ainsi qu'une documentation exhaustive pour guider les développeurs et les IA.

**Dépôt GitHub :** [https://github.com/AstekGroup/ai-agent-google-adk-template](https://github.com/AstekGroup/ai-agent-google-adk-template)

## 🚀 Démarrage rapide

```bash
# Cloner le dépôt
git clone https://github.com/AstekGroup/ai-agent-google-adk-template.git
cd ai-agent-google-adk-template

# Ou via SSH
git clone git@github.com:AstekGroup/ai-agent-google-adk-template.git
```

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

1. **Cloner le dépôt** : Utiliser `git clone` pour récupérer les templates
2. **Consulter la documentation** : Parcourir `resources/` pour comprendre Google ADK
3. **Choisir un template** : Voir `templates/README.md` pour la liste complète
4. **Copier et personnaliser** : Copier un template et l'adapter à vos besoins

### Pour les IA assistants

1. **Lire Agents.md** : Guide complet avec patterns et exemples
2. **Référencer resources/** : Documentation exhaustive de l'API
3. **Suivre les templates** : Exemples de code fonctionnels dans `templates/`

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

## Ressources externes

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
