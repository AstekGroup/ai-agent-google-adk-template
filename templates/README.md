# Index des Templates Google ADK

**Date : Novembre 2025**

## Vue d'ensemble

Cet index référence tous les templates disponibles pour créer des agents Google ADK. Chaque template est conçu pour un cas d'usage spécifique et peut être utilisé comme point de départ pour votre projet.

## Templates Python

### 1. Simple Agent
**Localisation** : `templates/python/simple-agent/`  
**Complexité** : ⭐ Débutant  
**Description** : Agent de base avec un outil simple  
**Cas d'usage** : Chatbot simple, assistant basique  
**Documentation** : [README.md](python/README.md)

### 2. Sequential Agent
**Localisation** : `templates/python/sequential-agent/`  
**Complexité** : ⭐⭐ Intermédiaire  
**Description** : Pipeline séquentiel d'agents  
**Cas d'usage** : Génération de contenu avec validation  
**Pattern** : Agent1 → Agent2 → Agent3

### 3. Parallel Agent
**Localisation** : `templates/python/parallel-agent/`  
**Complexité** : ⭐⭐ Intermédiaire  
**Description** : Agents parallèles avec fusion  
**Cas d'usage** : Recherche multi-sources, analyse comparative  
**Pattern** : [Agent1, Agent2, Agent3] → Merger

### 4. Loop Agent
**Localisation** : `templates/python/loop-agent/`  
**Complexité** : ⭐⭐⭐ Avancé  
**Description** : Boucle d'amélioration itérative  
**Cas d'usage** : Refinement de contenu, optimisation  
**Pattern** : Initial → [Critic → Refiner]×N

### 5. RAG Agent
**Localisation** : `templates/python/rag-agent/`  
**Complexité** : ⭐⭐ Intermédiaire  
**Description** : Agent avec RAG Vertex AI  
**Cas d'usage** : Q&A sur documentation, recherche contextuelle  
**Pattern** : Agent → RAG Tool → Vector Search

### 6. Custom Agent
**Localisation** : `templates/python/custom-agent/`  
**Complexité** : ⭐⭐⭐ Avancé  
**Description** : Agent personnalisé avec BaseAgent  
**Cas d'usage** : Workflows complexes personnalisés  
**Pattern** : Custom orchestration logic

## Templates Java

### 1. Simple Agent
**Localisation** : `templates/java/simple-agent/`  
**Complexité** : ⭐ Débutant  
**Description** : Agent de base avec Maven  
**Cas d'usage** : Agent conversationnel simple  
**Documentation** : [README.md](java/README.md)

### 2. Multi-Agent
**Localisation** : `templates/java/multi-agent/`  
**Complexité** : ⭐⭐⭐ Avancé  
**Description** : Orchestration multi-agents  
**Cas d'usage** : Systèmes complexes en Java  
**Pattern** : Sequential + Parallel patterns

## Guide de sélection rapide

### Je veux créer...

- **Un chatbot simple** → Simple Agent (Python ou Java)
- **Un pipeline de traitement** → Sequential Agent
- **Une recherche multi-sources** → Parallel Agent
- **Une amélioration itérative** → Loop Agent
- **Un Q&A sur documents** → RAG Agent
- **Un workflow personnalisé** → Custom Agent

## Utilisation

### 1. Choisir un template

Consulter la documentation de chaque template pour comprendre son cas d'usage.

### 2. Copier le template

```bash
# Python
cp -r templates/python/simple-agent/ my-new-agent/

# Java
cp -r templates/java/simple-agent/ my-new-agent/
```

### 3. Suivre le README

Chaque template contient un README.md avec :
- Instructions d'installation
- Guide d'utilisation
- Exemples de code
- Guide de personnalisation

## Personnalisation

Tous les templates peuvent être personnalisés :

1. **Modifier l'agent** : Adapter les instructions et capacités
2. **Ajouter des outils** : Intégrer de nouveaux outils
3. **Ajouter des callbacks** : Personnaliser le comportement
4. **Modifier la structure** : Adapter selon vos besoins

## Contribution

Pour ajouter un nouveau template :

1. Créer la structure dans `templates/python/` ou `templates/java/`
2. Suivre le [Guide de création](docs/CREATION_GUIDE.md)
3. Ajouter une entrée dans cet index
4. Documenter dans le README du template

## Ressources

- [Agents.md](../../Agents.md) - Guide complet pour les IA
- [Documentation ADK](../resources/)
- [Guide de création](docs/CREATION_GUIDE.md)
- [Documentation des templates](docs/README.md)
