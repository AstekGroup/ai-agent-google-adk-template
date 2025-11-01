# Guide rapide - Règles Cursor Google ADK

**🚀 Les règles Cursor sont maintenant actives dans ce repository !**

## ⚡ Démarrage rapide

### Que font ces règles ?

Elles permettent à l'IA assistant de Cursor de :
- ✅ Comprendre automatiquement ce repository de templates
- ✅ Vous guider dans le choix du bon template
- ✅ Créer des projets agents correctement configurés
- ✅ Générer du code conforme aux standards Google ADK

### Comment les utiliser ?

**C'est automatique !** Les règles sont déjà chargées par Cursor.

## 💬 Exemples de prompts

### Créer un agent simple

> "Je veux créer un agent simple qui peut donner la météo et l'heure"

L'IA va :
1. Choisir le template `simple-agent`
2. Copier le template dans un nouveau répertoire
3. Configurer le projet
4. Créer les outils météo et heure
5. Générer les tests

### Créer un pipeline de traitement

> "Je veux créer un agent qui écrit un article, le fait réviser, puis l'améliore"

L'IA va :
1. Identifier le pattern : **Sequential Agent**
2. Utiliser le template `sequential-agent`
3. Créer 3 sous-agents : Writer, Reviewer, Refiner
4. Configurer le pipeline
5. Générer les tests

### Créer un agent de recherche

> "Je veux un agent qui recherche en parallèle sur 3 sources différentes et combine les résultats"

L'IA va :
1. Identifier le pattern : **Parallel Agent**
2. Utiliser le template `parallel-agent`
3. Créer 3 agents de recherche parallèles
4. Configurer la fusion des résultats
5. Générer les tests

### Créer un agent d'amélioration itérative

> "Je veux un agent qui génère du code, le critique, et l'améliore jusqu'à ce qu'il soit satisfaisant"

L'IA va :
1. Identifier le pattern : **Loop Agent**
2. Utiliser le template `loop-agent`
3. Créer l'agent critique et l'agent d'amélioration
4. Configurer la condition de sortie
5. Générer les tests

### Créer un agent Q&A sur documents

> "Je veux un agent qui répond à des questions en cherchant dans une base de documents"

L'IA va :
1. Identifier le pattern : **RAG Agent**
2. Utiliser le template `rag-agent`
3. Configurer Vertex AI RAG
4. Créer l'agent avec retrieval
5. Générer les tests

## 📋 Templates disponibles

| Template | Niveau | Usage |
|----------|--------|-------|
| simple-agent | ⭐ Débutant | Agent simple avec outils |
| sequential-agent | ⭐⭐ Intermédiaire | Pipeline étape par étape |
| parallel-agent | ⭐⭐ Intermédiaire | Traitement parallèle |
| loop-agent | ⭐⭐⭐ Avancé | Amélioration itérative |
| rag-agent | ⭐⭐ Intermédiaire | Q&A sur documents |
| custom-agent | ⭐⭐⭐ Avancé | Logique personnalisée |

## 🎯 Ce que l'IA sait faire

### Configuration automatique
- ✅ Créer le fichier `.env` depuis `.env.example`
- ✅ Configurer `pyproject.toml` ou `pom.xml`
- ✅ Installer les dépendances
- ✅ Configurer les variables d'environnement

### Génération de code
- ✅ Agent principal avec instructions claires
- ✅ Outils personnalisés avec docstrings
- ✅ Sous-agents pour patterns multi-agents
- ✅ Callbacks si nécessaire
- ✅ Tests unitaires

### Best Practices
- ✅ Instructions d'agent claires et précises
- ✅ Gestion d'erreurs
- ✅ Type hints Python
- ✅ Docstrings complètes
- ✅ Sécurité (secrets via .env)

### Déploiement
- ✅ Script de déploiement Vertex AI
- ✅ Configuration Cloud Run
- ✅ Build du package wheel
- ✅ Tests de déploiement

## 🛠️ Commandes utiles

L'IA connaît toutes ces commandes :

### Python
```bash
# Installation
poetry install  # ou: uv sync

# Tests
poetry run pytest

# Build
poetry build --format=wheel --out-dir deployment
```

### Java
```bash
# Compilation
mvn clean install

# Tests
mvn test

# Package
mvn package
```

## 📖 Documentation

### Priorité 1 - Pour comprendre Google ADK
- `resources/01-overview.md` - Introduction
- `resources/02-architecture.md` - Architecture
- `Agents.md` - Guide complet pour IA

### Priorité 2 - Pour développer
- `.cursor/rules/google-adk-template.mdc` - Règles complètes
- `templates/` - Templates prêts à l'emploi
- `resources/05-examples-patterns.md` - Exemples

### Priorité 3 - Pour déployer
- `resources/06-deployment.md` - Guide déploiement
- `templates/python/simple-agent/deployment/` - Exemples

## 🎓 Workflow recommandé

### 1. Définir votre besoin
Décrivez ce que vous voulez créer à l'IA

### 2. L'IA choisit le template
Elle identifie le pattern approprié

### 3. Création du projet
L'IA copie et configure le template

### 4. Personnalisation
Vous adaptez selon vos besoins spécifiques

### 5. Tests
L'IA génère et exécute les tests

### 6. Déploiement
L'IA prépare les scripts de déploiement

## ⚙️ Configuration Google Cloud

### Option 1 : AI Studio (développement)
```bash
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=your-api-key
```

Obtenir la clé : https://aistudio.google.com/apikey

### Option 2 : Vertex AI (production)
```bash
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```

## 🔍 Dépannage

### L'IA ne comprend pas mon besoin
- Soyez plus précis sur le workflow souhaité
- Mentionnez les étapes de traitement
- Donnez des exemples d'utilisation

### L'IA choisit le mauvais template
- Précisez le type d'orchestration (séquentiel, parallèle, boucle)
- Mentionnez si c'est simple ou complexe
- Indiquez le nombre d'agents nécessaires

### Erreur de configuration
- L'IA connaît les erreurs courantes
- Elle peut vous aider à configurer `.env`
- Elle sait tester la configuration

## 📞 Besoin d'aide ?

### Pour les règles Cursor
- Voir `.cursor/README.md`
- Voir `.cursor/RULES_INFO.md`

### Pour Google ADK
- Voir `Agents.md`
- Voir `resources/`
- https://google.github.io/adk-docs/

### Pour les templates
- Voir `templates/README.md`
- Voir `templates/docs/CREATION_GUIDE.md`

## 🚦 Indicateurs de succès

Vous savez que ça fonctionne quand :
- ✅ L'IA identifie le bon template automatiquement
- ✅ Elle génère du code conforme aux standards
- ✅ Les tests passent du premier coup
- ✅ La configuration est correcte
- ✅ Le déploiement fonctionne

## 🎉 Prêt à commencer !

**Essayez maintenant** :
1. Ouvrez le chat Cursor
2. Décrivez l'agent que vous voulez créer
3. Laissez l'IA vous guider

**Exemple de premier prompt** :
> "Je veux créer un agent simple qui peut calculer des opérations mathématiques"

L'IA s'occupe du reste ! 🚀

---

**Note** : Ces règles sont spécifiques à ce repository de templates. Les projets créés depuis ces templates peuvent avoir leurs propres règles si nécessaire.

