# Informations sur les règles Cursor

**Date de création** : Novembre 2025

## Fichiers créés

### 1. `.cursor/rules/google-adk-template.mdc`
**Fichier principal de règles Cursor** - 600+ lignes

Contient :
- Vue d'ensemble du repository de templates
- Structure complète et organisation
- Principes fondamentaux Google ADK
- Guide d'utilisation des templates
- Patterns d'implémentation (Simple, Sequential, Parallel, Loop, RAG, Custom)
- Configuration environnement et variables
- Tests et déploiement
- Best practices et standards de qualité
- Commandes fréquentes
- Checklist de développement
- Messages d'erreur courants et solutions

### 2. `.cursor/README.md`
**Documentation des règles Cursor**

Explique :
- Contenu des règles
- Utilisation pour développeurs et IA
- Processus de création de projets
- Références à la documentation
- Maintenance et mise à jour

### 3. Modifications du `README.md` principal
**Ajout de la section Règles Cursor**

- Mise à jour de la structure du repository
- Ajout dans "Utilisation rapide pour les IA assistants"
- Nouvelle section "Règles Cursor" dans Documentation
- Mise à jour de la table des matières

## Objectifs des règles

### Pour les développeurs
- Aide contextuelle lors du développement avec Google ADK
- Accès rapide aux patterns et exemples
- Guidance sur les best practices
- Assistance dans le choix du template approprié

### Pour les IA assistants (Cursor)
- Compréhension complète du repository de templates
- Instructions précises pour créer de nouveaux projets
- Patterns de code pour chaque type d'agent
- Standards de qualité et validation
- Checklist de développement

## Structure des règles

```
.cursor/
├── README.md                   # Documentation des règles
├── RULES_INFO.md              # Ce fichier - Informations récapitulatives
└── rules/
    └── google-adk-template.mdc # Règles complètes
```

## Contenu des règles par section

### 1. Vue d'ensemble et structure (lignes 1-100)
- Description du repository
- Organisation GitHub
- Structure des fichiers
- Principes fondamentaux

### 2. Utilisation des templates (lignes 101-200)
- Processus de sélection
- Copie et personnalisation
- Structure projet créé
- Configuration initiale

### 3. Règles de développement (lignes 201-400)
- Configuration agents
- Création d'outils
- Patterns multi-agents
- Exécution et tests

### 4. Configuration et déploiement (lignes 401-500)
- Variables d'environnement
- Obtention clés API
- Déploiement Vertex AI
- Déploiement Cloud Run

### 5. Best practices et support (lignes 501-600+)
- Standards de qualité
- Gestionnaires de paquets
- Documentation de référence
- Messages d'erreur courants
- Checklist développement

## Utilisation recommandée

### Lors de la création d'un nouveau projet agent

1. L'IA lit automatiquement les règles Cursor
2. Elle comprend la structure du repository
3. Elle identifie le template approprié selon le besoin
4. Elle copie le template hors du repository
5. Elle personnalise la configuration
6. Elle adapte le code à votre cas d'usage
7. Elle crée les tests et la documentation

### Lors du développement

- Les règles fournissent des exemples de code
- Elles rappellent les best practices
- Elles guident sur la configuration
- Elles aident au débogage

### Lors du déploiement

- Instructions pour Vertex AI Agent Engine
- Configuration Cloud Run
- Scripts de build
- Validation du déploiement

## Maintenance

### Quand mettre à jour les règles

- Ajout de nouveaux templates dans le repository
- Nouveaux patterns ou best practices découverts
- Mise à jour de Google ADK (nouvelles versions)
- Retours d'expérience sur les projets créés
- Problèmes ou erreurs fréquemment rencontrées

### Comment mettre à jour

1. Éditer `.cursor/rules/google-adk-template.mdc`
2. Ajouter/modifier les sections concernées
3. Mettre à jour les exemples si nécessaire
4. Tester avec l'IA assistant
5. Documenter les changements dans ce fichier

## Copie dans d'autres repositories

Ce template peut être copié dans :
- `/Users/tfoutrein/DEV/INEAT/WORKSPACE/TEMPLATES/` (selon vos règles projet)
- Autres repositories de templates d'équipe
- Projets spécifiques nécessitant les règles

**Lors de la copie** :
- Le dossier `.cursor/` est copié automatiquement
- Les règles restent fonctionnelles dans le nouveau contexte
- Adapter les chemins si nécessaire

## Intégration avec règles utilisateur existantes

Ces règles sont **complémentaires** aux règles utilisateur définies :
- Règles générales de projet (DEVPLAN, ADR, PROJECT_VIBE_CONF)
- Règles frontend (Nuxt, etc.)
- Règles backend (NestJS, FastAPI, etc.)
- Règles monorepo

Les règles Google ADK s'appliquent spécifiquement lors de :
- L'utilisation de ce template repository
- La création de nouveaux agents Google ADK
- Le développement avec Google Agent Development Kit

## Références

### Documentation dans ce repository
- `Agents.md` - Guide complet IA
- `resources/` - Documentation exhaustive ADK
- `templates/` - Templates prêts à l'emploi
- `templates/docs/CREATION_GUIDE.md` - Guide création templates

### Documentation externe
- https://google.github.io/adk-docs/
- https://github.com/google/adk-samples
- https://github.com/GoogleCloudPlatform/agent-starter-pack

## Feedback et améliorations

Pour améliorer ces règles :
1. Identifier les cas non couverts
2. Collecter les questions fréquentes
3. Documenter les solutions
4. Ajouter des exemples
5. Mettre à jour les règles

---

**Créé par** : IA Assistant Cursor  
**Pour** : Template Repository Google ADK  
**Organisation** : AstekGroup  
**Date** : Novembre 2025

