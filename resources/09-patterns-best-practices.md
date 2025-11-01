# Patterns et Best Practices Google ADK

**Date : Novembre 2025**

Ce document récapitule les patterns d'architecture et les best practices pour développer des agents Google ADK efficaces et maintenables.

## Patterns d'architecture

### Pattern 1 : Agent Simple

**Description** : Agent unique avec outils

**Architecture** :
```
User → Runner → Agent → Tools → Response
```

**Cas d'usage** :
- Chatbots simples
- Assistants avec capacités limitées
- Prototypes rapides

**Exemple** :
```python
agent = Agent(
    model="gemini-2.5-flash",
    name="simple_agent",
    instruction="You are a helpful assistant.",
    tools=[tool1, tool2]
)
```

### Pattern 2 : Sequential Pipeline

**Description** : Chaîne d'agents exécutés séquentiellement

**Architecture** :
```
User → Runner → SequentialAgent → [Agent1 → Agent2 → Agent3] → Response
```

**Cas d'usage** :
- Pipeline de traitement (ex: Write → Review → Refine)
- Validation en étapes
- Workflows déterministes

**Exemple** :
```python
pipeline = SequentialAgent(
    name="processing_pipeline",
    sub_agents=[writer, reviewer, publisher]
)
```

**Avantages** :
- Contrôle total sur l'ordre d'exécution
- État passé entre agents via session.state
- Facile à déboguer

**Inconvénients** :
- Plus lent (séquentiel)
- Pas de parallélisation

### Pattern 3 : Parallel Execution

**Description** : Agents exécutés en parallèle puis fusion

**Architecture** :
```
User → Runner → ParallelAgent → [Agent1, Agent2, Agent3] → Merger → Response
```

**Cas d'usage** :
- Recherche multi-sources
- Analyse comparative
- Tâches indépendantes

**Exemple** :
```python
parallel_research = ParallelAgent(
    name="parallel_research",
    sub_agents=[researcher1, researcher2, researcher3]
)

pipeline = SequentialAgent(
    sub_agents=[parallel_research, merger_agent]
)
```

**Avantages** :
- Exécution rapide (parallèle)
- Idéal pour tâches indépendantes

**Inconvénients** :
- Plus complexe à orchestrer
- Nécessite un agent de fusion

### Pattern 4 : Iterative Loop

**Description** : Amélioration itérative jusqu'à condition

**Architecture** :
```
User → Runner → InitialAgent → LoopAgent → [Critic → Refiner]×N → Response
```

**Cas d'usage** :
- Refinement de contenu
- Optimisation itérative
- Amélioration jusqu'à critères

**Exemple** :
```python
loop = LoopAgent(
    name="refinement_loop",
    sub_agents=[critic, refiner],
    max_iterations=5
)
```

**Avantages** :
- Qualité améliorée itérativement
- Contrôle sur le nombre d'itérations

**Inconvénients** :
- Peut être coûteux (multiples appels LLM)
- Risque de boucle infinie sans limite

### Pattern 5 : RAG (Retrieval-Augmented Generation)

**Description** : Agent avec recherche vectorielle

**Architecture** :
```
User → Runner → Agent → RAG Tool → Vector Search → Context → Response
```

**Cas d'usage** :
- Q&A sur documentation
- Recherche contextuelle
- Agents avec connaissances spécialisées

**Exemple** :
```python
rag_tool = VertexAiRagRetrieval(
    name='retrieve_docs',
    rag_resources=[rag.RagResource(rag_corpus=corpus_id)],
    similarity_top_k=10
)

rag_agent = Agent(
    model='gemini-2.5-flash',
    instruction="Use RAG to find relevant information.",
    tools=[rag_tool]
)
```

### Pattern 6 : Custom Orchestration

**Description** : Logique d'orchestration personnalisée avec BaseAgent

**Architecture** :
```
User → Runner → CustomAgent → Custom Logic → Response
```

**Cas d'usage** :
- Workflows complexes
- Logique conditionnelle avancée
- Intégrations spécifiques

**Exemple** :
```python
class CustomAgent(BaseAgent):
    async def _run_async_impl(self, ctx):
        # Logique personnalisée
        if condition:
            yield from self.agent1.run_async(ctx)
        else:
            yield from self.agent2.run_async(ctx)
```

## Best Practices

### 1. Instructions claires

✅ **Bon** :
```python
instruction="""You are a weather assistant.
When users ask about weather:
1. Extract the city name
2. Use get_weather tool
3. Present results clearly

If city not found, apologize and suggest alternatives."""
```

❌ **Mauvais** :
```python
instruction="Help users with weather"
```

### 2. Outils bien documentés

✅ **Bon** :
```python
def get_weather(city: str, units: str = "celsius") -> dict:
    """
    Get current weather for a city.
    
    Args:
        city: City name (required)
        units: Temperature units - "celsius" or "fahrenheit"
    
    Returns:
        Dict with status, city, temperature, units, condition
    """
    ...
```

❌ **Mauvais** :
```python
def get_weather(city):
    ...
```

### 3. Gestion d'erreurs

✅ **Bon** :
```python
def api_call(endpoint: str, max_retries: int = 3) -> dict:
    for attempt in range(max_retries):
        try:
            response = requests.get(endpoint, timeout=10)
            response.raise_for_status()
            return {"status": "success", "data": response.json()}
        except Exception as e:
            if attempt == max_retries - 1:
                return {"status": "error", "message": str(e)}
            time.sleep(2 ** attempt)
```

❌ **Mauvais** :
```python
def api_call(endpoint):
    return requests.get(endpoint).json()
```

### 4. Gestion d'état

✅ **Bon** :
```python
def before_agent_callback(ctx: CallbackContext):
    if "user_preferences" not in ctx.state:
        ctx.state["user_preferences"] = {}
    
    # Initialiser avec valeurs par défaut
    ctx.state.setdefault("turn_count", 0)
    ctx.state["turn_count"] += 1
```

❌ **Mauvais** :
```python
def before_agent_callback(ctx):
    ctx.state["key"] = "value"  # Pas de vérification
```

### 5. Tests complets

✅ **Bon** :
```python
def test_agent_with_tool():
    # Arrange
    session = create_test_session()
    
    # Act
    events = runner.run(user_id="test", session_id="test", 
                       new_message=create_test_message())
    
    # Assert
    assert has_final_response(events)
    assert tool_was_called(events, "get_weather")
```

### 6. Configuration via variables d'environnement

✅ **Bon** :
```python
model = os.getenv("AGENT_MODEL", "gemini-2.5-flash")
max_iterations = int(os.getenv("MAX_ITERATIONS", "5"))
```

❌ **Mauvais** :
```python
model = "gemini-2.5-flash"  # Hardcodé
```

## Anti-patterns à éviter

### 1. Instructions trop vagues

❌ Ne pas faire :
```python
instruction="Help users"
```

✅ Faire :
```python
instruction="""You are a customer service agent for an e-commerce platform.
Your role is to:
- Answer product questions
- Handle returns and refunds
- Process orders

Be professional and helpful."""
```

### 2. Outils sans validation

❌ Ne pas faire :
```python
def update_database(query):
    execute(query)  # Injection SQL possible
```

✅ Faire :
```python
def update_database(table: str, id: int, data: dict):
    # Validation et sanitization
    validate_table_name(table)
    validate_id(id)
    sanitize_data(data)
    execute_safe_query(table, id, data)
```

### 3. Pas de gestion d'erreurs

❌ Ne pas faire :
```python
def get_data():
    return api.get("/endpoint").json()
```

✅ Faire :
```python
def get_data():
    try:
        response = api.get("/endpoint", timeout=10)
        response.raise_for_status()
        return {"status": "success", "data": response.json()}
    except Exception as e:
        return {"status": "error", "message": str(e)}
```

### 4. État non initialisé

❌ Ne pas faire :
```python
def callback(ctx):
    ctx.state["count"] += 1  # KeyError si non initialisé
```

✅ Faire :
```python
def callback(ctx):
    ctx.state["count"] = ctx.state.get("count", 0) + 1
```

## Performance

### Optimisations

1. **Cache des résultats coûteux**
```python
def before_tool_callback(tool_name, tool_args, ctx):
    cache_key = f"cache:{tool_name}:{hash(str(tool_args))}"
    cached = ctx.state.get(cache_key)
    if cached:
        return cached  # Retourner cache au lieu d'exécuter
```

2. **Parallélisation quand possible**
```python
# Utiliser ParallelAgent pour tâches indépendantes
parallel_agent = ParallelAgent(sub_agents=[task1, task2, task3])
```

3. **Limiter les itérations**
```python
loop = LoopAgent(
    sub_agents=[critic, refiner],
    max_iterations=5  # Toujours définir une limite
)
```

## Sécurité

### Bonnes pratiques

1. **Validation des entrées**
```python
from pydantic import BaseModel, validator

class Input(BaseModel):
    city: str
    
    @validator('city')
    def validate_city(cls, v):
        if not v or len(v) < 2:
            raise ValueError('City name too short')
        return v.strip().title()
```

2. **Gestion des secrets**
```python
# Utiliser variables d'environnement, jamais hardcodé
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY not set")
```

3. **Sanitization des réponses**
```python
def sanitize_response(text: str) -> str:
    # Supprimer caractères dangereux
    return text.replace("<script>", "").strip()
```

## Ressources

- [Agents.md](../../Agents.md) - Guide complet pour les IA
- [Documentation ADK](../resources/)
- [Exemples officiels](https://github.com/google/adk-samples)
