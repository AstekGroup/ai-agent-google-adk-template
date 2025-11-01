# Documentation des Templates Google ADK

**Date : Novembre 2025**

Cette documentation présente l'ensemble des templates disponibles pour créer des agents Google ADK.

## Vue d'ensemble

Les templates sont organisés par langage de programmation et par type de complexité. Chaque template inclut :
- Structure de projet complète
- Code d'exemple fonctionnel
- Configuration de déploiement
- Tests de base
- Documentation complète

## Templates disponibles

### Python

#### 1. Simple Agent (`templates/python/simple-agent/`)
- Agent de base avec un outil
- Configuration Poetry/uv
- Déploiement Vertex AI
- **Cas d'usage** : Agent conversationnel simple, chatbot de base

#### 2. Multi-Agent Sequential (`templates/python/sequential-agent/`)
- Pipeline séquentiel d'agents
- Exemple : Writer → Reviewer → Refiner
- **Cas d'usage** : Génération de contenu avec validation

#### 3. Multi-Agent Parallel (`templates/python/parallel-agent/`)
- Agents parallèles pour recherche
- Fusion des résultats
- **Cas d'usage** : Recherche multi-sources, analyse comparative

#### 4. Loop Agent (`templates/python/loop-agent/`)
- Boucle d'amélioration itérative
- Critic + Refiner pattern
- **Cas d'usage** : Amélioration itérative de contenu

#### 5. RAG Agent (`templates/python/rag-agent/`)
- Intégration Vertex AI RAG
- Recherche vectorielle
- **Cas d'usage** : Q&A sur documentation, recherche contextuelle

#### 6. Custom Agent (`templates/python/custom-agent/`)
- Agent personnalisé avec BaseAgent
- Logique d'orchestration avancée
- **Cas d'usage** : Workflows complexes personnalisés

### Java

#### 1. Simple Agent (`templates/java/simple-agent/`)
- Agent de base avec Maven
- Configuration standard
- **Cas d'usage** : Agent conversationnel simple

#### 2. Multi-Agent (`templates/java/multi-agent/`)
- Orchestration multi-agents
- Patterns séquentiels et parallèles
- **Cas d'usage** : Systèmes complexes en Java

## Structure commune

Tous les templates suivent cette structure :

```
template-name/
├── README.md               # Documentation spécifique
├── pyproject.toml          # ou pom.xml pour Java
├── .env.example           # Variables d'environnement
├── src/                   # Code source
│   └── agent_name/
│       ├── agent.py       # Agent principal
│       ├── tools/         # Outils
│       └── callbacks/     # Callbacks (si nécessaire)
├── tests/                 # Tests
├── deployment/            # Scripts de déploiement
└── docs/                  # Documentation additionnelle
```

## Guide de sélection

### Choisir un template selon vos besoins

1. **Agent simple** : Utiliser `simple-agent`
2. **Pipeline de traitement** : Utiliser `sequential-agent`
3. **Recherche parallèle** : Utiliser `parallel-agent`
4. **Amélioration itérative** : Utiliser `loop-agent`
5. **Q&A sur documents** : Utiliser `rag-agent`
6. **Logique personnalisée** : Utiliser `custom-agent`

## Utilisation des templates

### 1. Copier le template

```bash
# Python
cp -r templates/python/simple-agent/ my-new-agent/

# Java
cp -r templates/java/simple-agent/ my-new-agent/
```

### 2. Installer les dépendances

```bash
# Python avec Poetry
cd my-new-agent
poetry install

# Python avec uv
cd my-new-agent
uv sync

# Java avec Maven
cd my-new-agent
mvn clean install
```

### 3. Configurer l'environnement

```bash
cp .env.example .env
# Éditer .env avec vos valeurs
```

### 4. Personnaliser

- Modifier l'agent principal
- Ajouter des outils
- Adapter les instructions
- Personnaliser les callbacks

### 5. Tester

```bash
# Python
pytest tests/

# Java
mvn test
```

### 6. Déployer

```bash
# Vertex AI Agent Engine
cd deployment
python deploy.py --create

# Cloud Run (voir Dockerfile)
gcloud run deploy ...
```

## Patterns d'architecture

### Pattern 1 : Agent Simple

```
User → Agent → Tool → Response
```

### Pattern 2 : Séquentiel

```
User → Agent1 → Agent2 → Agent3 → Response
```

### Pattern 3 : Parallèle

```
User → ParallelAgent → [Agent1, Agent2, Agent3] → Merger → Response
```

### Pattern 4 : Boucle

```
User → InitialAgent → [Critic → Refiner]×N → Response
```

### Pattern 5 : RAG

```
User → Agent → RAG Tool → Vector Search → Context → Response
```

## Bonnes pratiques

### 1. Instructions claires

- Décrire précisément le rôle de l'agent
- Indiquer les capacités et limites
- Fournir des exemples de comportement

### 2. Outils bien définis

- Descriptions claires et complètes
- Types de paramètres explicites
- Gestion d'erreurs robuste

### 3. Gestion d'état

- Utiliser les callbacks pour initialisation
- Persister l'état important
- Nettoyer l'état si nécessaire

### 4. Tests

- Tests unitaires pour chaque composant
- Tests d'intégration pour workflows
- Tests de bout en bout pour scénarios

### 5. Déploiement

- Configuration via variables d'environnement
- Scripts de déploiement automatisés
- Monitoring et logging

## Ressources

- [Agents.md](../../Agents.md) - Guide complet pour les IA
- [Documentation ADK](../resources/)
- [Exemples officiels](https://github.com/google/adk-samples)

## Support

Pour toute question sur les templates :
1. Consulter la documentation dans `resources/`
2. Voir les exemples dans `adk-samples`
3. Référencer `Agents.md` pour les patterns
