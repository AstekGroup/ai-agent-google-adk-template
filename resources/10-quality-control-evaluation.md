# Contrôle Qualité et Évaluation dans Google ADK

**Date : Novembre 2025**

Ce document décrit les fonctionnalités intégrées de contrôle qualité et d'évaluation dans le framework Google Agent Development Kit (ADK), permettant d'assurer la fiabilité, la sécurité et la performance des agents développés.

## Vue d'ensemble

Google ADK offre un framework complet d'évaluation et de contrôle qualité permettant d'analyser la performance des agents selon plusieurs dimensions :

- **Analyse de trajectoire** : Examine les schémas de prise de décision des agents
- **Validation des réponses** : Vérifie la qualité et la pertinence des réponses
- **Audit d'exécution pas à pas** : Permet de suivre chaque étape du processus d'exécution
- **Évaluation des performances** : Mesure les performances selon divers critères de sécurité et de qualité

## Architecture d'évaluation

### Composants principaux

#### 1. AgentEvaluator

L'`AgentEvaluator` est la classe principale pour l'évaluation programmatique des agents :

```python
from google.adk.evaluation.agent_evaluator import AgentEvaluator
import pytest

@pytest.mark.asyncio
async def test_with_single_test_file():
    """Test l'agent via un fichier de session."""
    await AgentEvaluator.evaluate(
        agent_module="home_automation_agent",
        eval_dataset_file_path_or_dir="tests/integration/fixture/home_automation_agent/simple_test.test.json",
    )
```

#### 2. Format de test (Test Files)

Les tests d'évaluation sont définis dans des fichiers JSON suivant un schéma Pydantic :

```json
{
  "eval_set_id": "home_automation_agent_light_on_off_set",
  "name": "",
  "description": "Ensemble d'évaluation pour tester le comportement `x` de l'agent",
  "eval_cases": [
    {
      "eval_id": "eval_case_id",
      "conversation": [
        {
          "invocation_id": "b7982664-0ab6-47cc-ab13-326656afdf75", 
          "user_content": {
            "parts": [
              {
                "text": "Turn off device_2 in the Bedroom."
              }
            ],
            "role": "user"
          },
          "final_response": {
            "parts": [
              {
                "text": "I have set the device_2 status to off."
              }
            ],
            "role": "model"
          },
          "intermediate_data": {
            "tool_uses": [
              {
                "args": {
                  "location": "Bedroom",
                  "device_id": "device_2",
                  "status": "OFF"
                },
                "name": "set_device_info"
              }
            ],
            "intermediate_responses": [] 
          }
        }
      ],
      "session_input": {
        "app_name": "home_automation_agent",
        "user_id": "test_user",
        "state": {}
      }
    }
  ]
}
```

## Critères d'évaluation

Google ADK fournit plusieurs critères d'évaluation intégrés que vous pouvez configurer dans vos fichiers de test.

### 1. Évaluation basée sur rubriques (Rubric-Based Evaluation)

#### `rubric_based_final_response_quality_v1`

Évalue la qualité des réponses finales de l'agent selon des rubriques personnalisées :

```json
{
  "criteria": {
    "rubric_based_final_response_quality_v1": {
      "threshold": 0.8,
      "judge_model_options": {
        "judge_model": "gemini-2.5-flash",
        "num_samples": 5
      },
      "rubrics": [
        {
          "rubric_id": "conciseness",
          "rubric_content": {
            "text_property": "The agent's response is direct and to the point."
          }
        },
        {
          "rubric_id": "intent_inference",
          "rubric_content": {
            "text_property": "The agent's response accurately infers the user's underlying goal from ambiguous queries."
          }
        }
      ]
    }
  }
}
```

**Paramètres** :
- `threshold` : Score minimum acceptable (0.0 à 1.0)
- `judge_model` : Modèle LLM utilisé pour l'évaluation
- `num_samples` : Nombre d'échantillons pour l'évaluation LLM
- `rubrics` : Liste de rubriques d'évaluation personnalisées

#### `rubric_based_tool_use_quality_v1`

Évalue la qualité de l'utilisation des outils par l'agent :

```json
{
  "criteria": {
    "rubric_based_tool_use_quality_v1": {
      "threshold": 1.0,
      "judge_model_options": {
        "judge_model": "gemini-2.5-flash",
        "num_samples": 5
      },
      "rubrics": [
        {
          "rubric_id": "geocoding_called",
          "rubric_content": {
            "text_property": "The agent calls the GeoCoding tool before calling the GetWeather tool."
          }
        },
        {
          "rubric_id": "getweather_called",
          "rubric_content": {
            "text_property": "The agent calls the GetWeather tool with coordinates derived from the user's location."
          }
        }
      ]
    }
  }
}
```

### 2. Détection des hallucinations (`hallucinations_v1`)

Vérifie que les réponses de l'agent sont bien fondées sur le contexte fourni :

```json
{
  "criteria": {
    "hallucinations_v1": {
      "threshold": 0.8,
      "judge_model_options": {
        "judge_model": "gemini-2.5-flash"
      },
      "evaluate_intermediate_nl_responses": true
    }
  }
}
```

**Paramètres** :
- `threshold` : Score minimum acceptable
- `evaluate_intermediate_nl_responses` : Évalue également les réponses intermédiaires (pas seulement la réponse finale)

### 3. Score de correspondance des réponses (`response_match_score`)

Mesure la similarité entre la réponse de l'agent et une réponse de référence en utilisant ROUGE-1 :

```json
{
  "criteria": {
    "response_match_score": 0.8
  }
}
```

ROUGE-1 calcule le chevauchement des unigrammes entre la réponse générée et la référence.

### 4. Score moyen de trajectoire des outils (`tool_trajectory_avg_score`)

Évalue la séquence d'utilisation des outils par l'agent :

```json
{
  "criteria": {
    "tool_trajectory_avg_score": 1.0
  }
}
```

Compare la trajectoire réelle des outils avec la trajectoire attendue.

### 5. Configuration combinée

Vous pouvez combiner plusieurs critères dans un même fichier de configuration :

```json
{
  "criteria": {
    "tool_trajectory_avg_score": 1.0,
    "response_match_score": 0.8,
    "rubric_based_final_response_quality_v1": {
      "threshold": 0.8,
      "judge_model_options": {
        "judge_model": "gemini-2.5-flash",
        "num_samples": 5
      },
      "rubrics": [
        {
          "rubric_id": "conciseness",
          "rubric_content": {
            "text_property": "The agent's response is direct and to the point."
          }
        }
      ]
    }
  }
}
```

## Utilisation des outils d'évaluation

### 1. Évaluation via CLI

La méthode la plus simple pour évaluer un agent est d'utiliser la commande CLI :

```bash
adk eval \
    <AGENT_MODULE_FILE_PATH> \
    <EVAL_SET_FILE_PATH> \
    [--config_file_path=<PATH_TO_TEST_JSON_CONFIG_FILE>] \
    [--print_detailed_results]
```

**Exemple** :

```bash
adk eval \
    samples_for_testing/hello_world \
    samples_for_testing/hello_world/hello_world_eval_set_001.evalset.json
```

**Options** :
- `--config_file_path` : Chemin vers le fichier de configuration JSON avec les critères d'évaluation
- `--print_detailed_results` : Affiche les résultats détaillés dans la console

### 2. Évaluation programmatique (Python)

Pour intégrer l'évaluation dans vos tests ou pipelines CI/CD :

```python
from google.adk.evaluation.agent_evaluator import AgentEvaluator
import pytest

@pytest.mark.asyncio
async def test_agent_basic():
    """Test les capacités de base de l'agent via un fichier de session."""
    await AgentEvaluator.evaluate(
        agent_module="home_automation_agent",
        eval_dataset_file_path_or_dir="tests/integration/fixture/home_automation_agent/simple_test.test.json",
    )
```

### 3. Exécution avec pytest

Les tests peuvent être exécutés via pytest dans vos pipelines de test :

```bash
pytest tests/integration/
```

### 4. Migration de données d'évaluation

Pour migrer des fichiers de test vers le nouveau schéma Pydantic :

```python
from google.adk.evaluation.agent_evaluator import AgentEvaluator

AgentEvaluator.migrate_eval_data_to_new_schema(
    old_test_data_file='path/to/your/old_test.json',
    optional_initial_session_file='path/to/your/initial_session.json',
    output_file='path/to/your/new_schema_output.json'
)
```

## Surveillance et observabilité en temps réel

Google ADK offre plusieurs mécanismes pour surveiller et observer le comportement des agents en temps réel.

### 1. InvocationContext

Suit l'état d'exécution et les décisions prises par l'agent pendant l'invocation :

```python
from google.adk.agents.invocation_context import InvocationContext

class CustomAgent(BaseAgent):
    async def _run_async_impl(self, ctx: InvocationContext):
        # Accéder au contexte d'invocation
        invocation_id = ctx.invocation_id
        agent_name = ctx.agent.name
        session_state = ctx.session.state
        # ...
```

**Propriétés disponibles** :
- `invocation_id` : Identifiant unique de l'invocation
- `agent` : Référence à l'agent en cours d'exécution
- `session` : Session utilisateur actuelle
- `state` : État de la session

### 2. CallbackContext

Fournit un accès à l'état de la session et au contexte de l'agent dans les callbacks :

```python
from google.adk.agents.callback_context import CallbackContext

def before_agent_callback(ctx: CallbackContext):
    # Accéder à l'état de session
    if "user_preferences" not in ctx.state:
        ctx.state["user_preferences"] = {}
    
    # Modifier les instructions dynamiquement
    if ctx.state.get("lang") == "fr":
        ctx._invocation_context.agent.instruction += "\nRépondez en français."
    
    return None

def after_agent_callback(ctx: CallbackContext):
    # Logger les résultats
    response = ctx._invocation_context.response
    ctx.state["last_response"] = response
    
    # Mettre à jour les métriques
    ctx.state["turn_count"] = ctx.state.get("turn_count", 0) + 1
    
    return None
```

### 3. Types de callbacks

#### Callbacks d'agent

**Before Agent Callback** :
```python
def before_agent_callback(ctx: CallbackContext):
    # Exécuté avant l'exécution de l'agent
    # Peut modifier les instructions, initialiser l'état
    return None
```

**After Agent Callback** :
```python
def after_agent_callback(ctx: CallbackContext):
    # Exécuté après l'exécution de l'agent
    # Peut logger, mettre à jour les métriques, modifier les réponses
    return None
```

#### Callbacks d'outils

**Before Tool Callback** :
```python
from google.adk.tools import ToolContext

async def before_tool_callback(tool_context: ToolContext):
    # Audit logging
    tool_name = tool_context.tool_name
    tool_args = tool_context.tool_args
    
    # Validation asynchrone
    if tool_args.get("operation") == "divide" and tool_args.get("divisor") == 0:
        # Bloquer l'opération invalide
        tool_context.actions.skip = True
        return {"error": "Division by zero not allowed"}
    
    return None
```

**After Tool Callback** :
```python
async def after_tool_callback(tool_context: ToolContext):
    # Amélioration de la réponse
    tool_result = tool_context.tool_result
    
    # Enrichir le résultat
    if tool_result.get("status") == "success":
        tool_result["enhanced"] = True
        tool_result["timestamp"] = time.time()
    
    return tool_result
```

#### Callbacks de modèle

**Before Model Callback** :
```python
def before_model_callback(ctx: CallbackContext):
    # Exécuté avant l'appel au modèle LLM
    # Peut modifier la configuration de génération
    return None
```

**After Model Callback** :
```python
def after_model_callback(ctx: CallbackContext):
    # Exécuté après l'appel au modèle LLM
    # Peut analyser, logger, modifier la réponse
    return None
```

### 4. Exemple complet : Surveillance avec callbacks

```python
from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools import ToolContext

def audit_callback(ctx: CallbackContext):
    """Callback pour audit et logging."""
    invocation_id = ctx._invocation_context.invocation_id
    agent_name = ctx._invocation_context.agent.name
    
    # Logger l'invocation
    logger.info(f"Agent {agent_name} invoked: {invocation_id}")
    
    # Tracker les métriques
    ctx.state["total_invocations"] = ctx.state.get("total_invocations", 0) + 1
    
    return None

async def validate_tool_callback(tool_context: ToolContext):
    """Validation et sécurité des outils."""
    tool_name = tool_context.tool_name
    tool_args = tool_context.tool_args
    
    # Vérification de sécurité
    if tool_name == "database_update" and not tool_args.get("user_id"):
        tool_context.actions.skip = True
        return {"error": "Unauthorized: user_id required"}
    
    # Audit logging
    logger.info(f"Tool {tool_name} called with args: {tool_args}")
    
    return None

agent = Agent(
    model="gemini-2.5-flash",
    name="monitored_agent",
    instruction="You are a helpful assistant.",
    before_agent_callback=audit_callback,
    after_agent_callback=audit_callback,
    before_tool_callback=validate_tool_callback
)
```

## Analyse de trajectoire

L'analyse de trajectoire permet de comparer les étapes d'exécution réelles de l'agent avec une séquence attendue.

### Concept

La trajectoire représente la séquence d'actions (appels d'outils, décisions) prises par l'agent pour répondre à une requête.

### Exemple de comparaison

```python
# Trajectoire attendue
expected_steps = [
    "determine_intent",
    "use_tool",
    "review_results",
    "report_generation"
]

# Trajectoire réelle (extrait des événements)
actual_steps = [
    "determine_intent",
    "use_tool",
    "review_results",
    "report_generation"
]

# L'évaluation compare ces deux séquences
```

### Configuration de l'évaluation de trajectoire

Dans votre fichier de test, définissez la trajectoire attendue dans `intermediate_data.tool_uses` :

```json
{
  "intermediate_data": {
    "tool_uses": [
      {
        "name": "geocoding_tool",
        "args": {"location": "Paris"}
      },
      {
        "name": "weather_tool",
        "args": {"coordinates": "...", "city": "Paris"}
      }
    ]
  }
}
```

## Sécurité et contrôles réseau

### VPC-SC (Virtual Private Cloud Service Controls)

Pour renforcer la sécurité, l'ADK peut être exécuté au sein d'un périmètre VPC-SC :

- **Isolation réseau** : Toutes les requêtes API restent confinées au périmètre
- **Réduction du risque d'exfiltration** : Empêche l'accès non autorisé aux ressources externes
- **Contrôle d'accès** : Les identités et périmètres offrent des contrôles généraux sur les actions des agents

### Garde-fous spécifiques aux outils

Les garde-fous permettent aux développeurs de définir précisément les actions autorisées :

```python
async def tool_guard(tool_context: ToolContext):
    """Garde-fou pour contrôler l'utilisation des outils."""
    tool_name = tool_context.tool_name
    tool_args = tool_context.tool_args
    
    # Liste blanche d'outils autorisés
    allowed_tools = ["get_weather", "search_docs"]
    if tool_name not in allowed_tools:
        tool_context.actions.skip = True
        return {"error": f"Tool {tool_name} not allowed"}
    
    # Validation des arguments
    if tool_name == "database_update":
        required_fields = ["user_id", "operation"]
        if not all(field in tool_args for field in required_fields):
            tool_context.actions.skip = True
            return {"error": "Missing required fields"}
    
    return None
```

## Intégration avec les pipelines CI/CD

### 1. Tests automatisés

Créez des tests pytest qui exécutent les évaluations :

```python
# tests/test_evaluation.py
import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator

@pytest.mark.asyncio
async def test_agent_quality():
    """Test de qualité de l'agent."""
    await AgentEvaluator.evaluate(
        agent_module="my_agent",
        eval_dataset_file_path_or_dir="tests/eval_sets/basic_quality.evalset.json",
        config_file_path="tests/eval_configs/quality_config.json"
    )
```

### 2. Pipeline GitHub Actions

```yaml
# .github/workflows/evaluate.yml
name: Evaluate Agent

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  evaluate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install uv
          uv sync
      
      - name: Run evaluations
        run: |
          adk eval \
            src/my_agent \
            tests/eval_sets/basic_quality.evalset.json \
            --config_file_path=tests/eval_configs/quality_config.json \
            --print_detailed_results
```

### 3. Storage des résultats

Les résultats d'évaluation peuvent être stockés dans Google Cloud Storage :

```bash
adk eval \
    src/my_agent \
    tests/eval_sets/basic_quality.evalset.json \
    --eval_storage_uri=gs://my-bucket/eval-results/
```

## Best Practices

### 1. Créer des ensembles d'évaluation complets

✅ **Bon** :
- Couvrir différents scénarios (succès, erreurs, cas limites)
- Inclure des tests pour chaque fonctionnalité principale
- Varier la complexité des requêtes

❌ **Mauvais** :
- Seulement des cas de succès simples
- Pas de tests d'erreur

### 2. Définir des seuils appropriés

✅ **Bon** :
```json
{
  "criteria": {
    "response_match_score": 0.8,  // Tolérance raisonnable
    "hallucinations_v1": {
      "threshold": 0.9  // Tolérance faible pour hallucinations
    }
  }
}
```

❌ **Mauvais** :
```json
{
  "criteria": {
    "response_match_score": 1.0  // Trop strict, impossible à atteindre
  }
}
```

### 3. Utiliser des rubriques spécifiques

✅ **Bon** :
```json
{
  "rubric_id": "geocoding_called",
  "rubric_content": {
    "text_property": "The agent calls the GeoCoding tool before calling the GetWeather tool."
  }
}
```

❌ **Mauvais** :
```json
{
  "rubric_id": "good_response",
  "rubric_content": {
    "text_property": "The agent responds well."
  }
}
```

### 4. Logger les métriques importantes

✅ **Bon** :
```python
def after_agent_callback(ctx: CallbackContext):
    # Tracker les métriques
    ctx.state["total_turns"] = ctx.state.get("total_turns", 0) + 1
    ctx.state["avg_response_time"] = calculate_avg_time(ctx)
    
    # Logger pour analyse
    logger.info(f"Agent {ctx._invocation_context.agent.name} completed turn")
    return None
```

### 5. Valider les outils avant exécution

✅ **Bon** :
```python
async def before_tool_callback(tool_context: ToolContext):
    # Valider les arguments
    if tool_context.tool_name == "database_update":
        if not validate_permissions(tool_context.tool_args):
            tool_context.actions.skip = True
            return {"error": "Insufficient permissions"}
    return None
```

## Exemples d'utilisation

### Exemple 1 : Évaluation de base

```bash
# Créer un fichier de test
cat > tests/eval_sets/basic_test.evalset.json << EOF
{
  "eval_set_id": "basic_test",
  "eval_cases": [
    {
      "eval_id": "test_1",
      "conversation": [
        {
          "user_content": {
            "parts": [{"text": "Hello"}],
            "role": "user"
          },
          "final_response": {
            "parts": [{"text": "Hello! How can I help you?"}],
            "role": "model"
          }
        }
      ],
      "session_input": {
        "app_name": "my_agent",
        "user_id": "test_user",
        "state": {}
      }
    }
  ]
}
EOF

# Exécuter l'évaluation
adk eval src/my_agent tests/eval_sets/basic_test.evalset.json
```

### Exemple 2 : Évaluation avec critères personnalisés

```bash
# Créer un fichier de configuration
cat > tests/eval_configs/custom_criteria.json << EOF
{
  "criteria": {
    "rubric_based_final_response_quality_v1": {
      "threshold": 0.85,
      "judge_model_options": {
        "judge_model": "gemini-2.5-flash",
        "num_samples": 3
      },
      "rubrics": [
        {
          "rubric_id": "helpfulness",
          "rubric_content": {
            "text_property": "The agent's response is helpful and addresses the user's query."
          }
        },
        {
          "rubric_id": "accuracy",
          "rubric_content": {
            "text_property": "The agent's response contains accurate information."
          }
        }
      ]
    },
    "hallucinations_v1": {
      "threshold": 0.9,
      "judge_model_options": {
        "judge_model": "gemini-2.5-flash"
      }
    }
  }
}
EOF

# Exécuter avec configuration
adk eval \
    src/my_agent \
    tests/eval_sets/basic_test.evalset.json \
    --config_file_path=tests/eval_configs/custom_criteria.json \
    --print_detailed_results
```

### Exemple 3 : Intégration dans pytest

```python
# tests/test_agent_quality.py
import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator

class TestAgentQuality:
    @pytest.mark.asyncio
    async def test_response_quality(self):
        """Test la qualité des réponses."""
        await AgentEvaluator.evaluate(
            agent_module="my_agent",
            eval_dataset_file_path_or_dir="tests/eval_sets/response_quality.evalset.json",
            config_file_path="tests/eval_configs/quality_config.json"
        )
    
    @pytest.mark.asyncio
    async def test_tool_usage(self):
        """Test l'utilisation correcte des outils."""
        await AgentEvaluator.evaluate(
            agent_module="my_agent",
            eval_dataset_file_path_or_dir="tests/eval_sets/tool_usage.evalset.json",
            config_file_path="tests/eval_configs/tool_config.json"
        )
    
    @pytest.mark.asyncio
    async def test_hallucination_detection(self):
        """Test la détection des hallucinations."""
        await AgentEvaluator.evaluate(
            agent_module="my_agent",
            eval_dataset_file_path_or_dir="tests/eval_sets/hallucination_test.evalset.json",
            config_file_path="tests/eval_configs/hallucination_config.json"
        )
```

## Ressources supplémentaires

- [Documentation officielle ADK - Évaluation](https://google.github.io/adk-docs/evaluate)
- [Documentation officielle ADK - Critères d'évaluation](https://google.github.io/adk-docs/evaluate/criteria)
- [Documentation officielle ADK - Agents responsables](https://google.github.io/adk-docs/3.6-responsible-agents)
- [GitHub ADK Python](https://github.com/google/adk-python)
- [GitHub ADK Samples](https://github.com/google/adk-samples)

## Conclusion

Le framework d'évaluation et de contrôle qualité intégré à Google ADK offre :

- **Évaluation complète** : Critères multiples pour évaluer différents aspects des agents
- **Surveillance en temps réel** : Callbacks et contextes pour observer le comportement
- **Sécurité** : Garde-fous et contrôles réseau pour protéger les ressources
- **Intégration facile** : CLI et API programmatique pour intégrer dans les pipelines CI/CD

Ces outils permettent de garantir que les agents développés sont fiables, sécurisés et performants avant leur déploiement en production.

