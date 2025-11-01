# Documentation du template Simple Agent

## Architecture

```
User → Runner → Simple Agent → Weather Tool → Response
```

## Composants

### Agent Principal
- **Fichier** : `src/simple_agent/agent.py`
- **Modèle** : gemini-2.5-flash
- **Outils** : get_weather

### Outil Météo
- **Fichier** : `src/simple_agent/tools.py`
- **Fonction** : get_weather(city, units)
- **Note** : Implémentation mock, à remplacer par vraie API

## Personnalisation

### 1. Changer le modèle

Dans `src/simple_agent/agent.py` :
```python
root_agent = Agent(
    model="gemini-2.5-pro",  # Changer ici
    ...
)
```

### 2. Ajouter un outil

1. Créer la fonction dans `tools.py`
2. Créer l'outil avec `FunctionTool`
3. Ajouter à la liste `tools` dans `agent.py`

### 3. Modifier les instructions

Adapter les instructions dans `agent.py` selon votre cas d'usage.

## Intégration avec vraie API météo

Pour intégrer une vraie API météo (ex: OpenWeatherMap) :

```python
import requests

def get_weather(city: str, units: str = "celsius") -> dict:
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric" if units == "celsius" else "imperial"
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "status": "success",
            "city": city,
            "temperature": str(data["main"]["temp"]),
            "units": units,
            "condition": data["weather"][0]["description"]
        }
    else:
        return {"status": "error", "message": "API error"}
```

## Tests

Les tests dans `tests/test_agent.py` couvrent :
- Création de l'agent
- Interaction basique
- Fonctionnement de l'outil météo
- Requête météo complète

## Déploiement

### Prérequis

1. Build le package :
```bash
poetry build --format=wheel --out-dir deployment
```

2. Configurer les variables :
```bash
export GOOGLE_CLOUD_PROJECT=your-project-id
export GOOGLE_CLOUD_LOCATION=us-central1
```

3. Déployer :
```bash
cd deployment
python deploy.py
```

### Test du déploiement

```bash
python test_deployment.py --resource_id=$RESOURCE_ID
```
