# Règles Cursor pour Google ADK Template

Ce répertoire contient les règles Cursor pour faciliter le développement avec les templates Google ADK.

## Fichiers de règles

### `rules/google-adk-template.mdc`

Fichier principal de règles Cursor qui fournit :

- **Compréhension du repository** : Structure et organisation du template repository
- **Utilisation des templates** : Comment copier et personnaliser les templates
- **Patterns Google ADK** : Tous les patterns d'agents (simple, sequential, parallel, loop, RAG, custom)
- **Configuration** : Variables d'environnement, gestionnaires de paquets
- **Best practices** : Standards de code, sécurité, performance
- **Déploiement** : Vertex AI Agent Engine et Cloud Run
- **Commandes fréquentes** : Développement, tests, build

## Utilisation

Les règles Cursor sont automatiquement chargées par l'éditeur Cursor lorsque vous travaillez dans ce repository.

### Pour les développeurs

Les règles Cursor aident l'IA à :
- Comprendre la structure du repository de templates
- Proposer le bon template selon vos besoins
- Générer du code conforme aux standards Google ADK
- Créer de nouveaux projets agents correctement configurés
- Suivre les best practices

### Pour les IA assistants

Les règles fournissent :
- Contexte complet du repository
- Instructions pour utiliser les templates
- Exemples de code pour chaque pattern
- Checklist de développement
- Références à la documentation

## Création de nouveaux projets

Lorsque vous demandez à l'IA de créer un nouveau projet agent, elle :

1. **Identifiera le template approprié** selon vos besoins
2. **Copiera le template** dans un nouveau répertoire (HORS de ce repository)
3. **Personnalisera** la configuration (pyproject.toml, .env, etc.)
4. **Adaptera** l'agent et les outils à votre cas d'usage
5. **Créera** les tests et la documentation

## Documentation de référence

Les règles Cursor font référence à :

- **Agents.md** : Guide complet pour les IA développant avec ADK
- **resources/** : Documentation exhaustive de Google ADK
- **templates/** : Templates prêts à l'emploi
- **templates/docs/CREATION_GUIDE.md** : Guide de création de templates

## Maintenance

### Mise à jour des règles

Lorsque vous mettez à jour le repository (nouveaux templates, patterns, etc.), pensez à mettre à jour également `rules/google-adk-template.mdc`.

### Copie dans les projets

Lorsque vous copiez ce template dans `/Users/tfoutrein/DEV/INEAT/WORKSPACE/TEMPLATES/` ou ailleurs, le fichier de règles sera également copié et utilisable dans les nouveaux projets.

## Structure recommandée pour les projets créés

Les projets créés depuis ces templates **ne doivent PAS** inclure les règles Cursor du template, mais peuvent avoir leurs propres règles spécifiques au projet.

---

**Note** : Ces règles sont spécifiques au repository de templates. Les projets agents créés depuis ces templates auront leurs propres configurations Cursor si nécessaire.

