# Templates Java - Agents Google ADK

**Version : 1.0.0**  
**Date : Novembre 2025**  
**Langage : Java 17+**

## Description

Cette section contient des templates pour créer des agents Google ADK en Java. Chaque template inclut :
- Configuration Maven complète
- Structure de projet standardisée
- Exemples d'implémentation
- Tests unitaires
- Configuration Docker pour déploiement

## Templates disponibles

### simple-agent

Template de base pour créer un agent Google ADK simple avec un outil personnalisé.

**⭐ Niveau : Débutant**

- [Documentation complète](simple-agent/README.md)
- Agent simple avec outil météo
- Configuration Maven complète
- Tests unitaires
- Dockerfile inclus

**Fichiers principaux :**
- `SimpleAgent.java` - Agent principal
- `WeatherTool.java` - Exemple d'outil personnalisé
- `Main.java` - Point d'entrée
- `SimpleAgentTest.java` - Tests unitaires

**Utilisation rapide :**

```bash
cd simple-agent
mvn clean install
java -jar target/simple-agent-1.0.0.jar
```

Pour plus de détails, consultez [simple-agent/README.md](simple-agent/README.md).

## Structure du projet

```
simple-agent-java/
├── pom.xml                 # Configuration Maven
├── README.md
├── .env.example
├── .gitignore
├── src/
│   └── main/
│       ├── java/
│       │   └── com/google/adk/samples/simpleagent/
│       │       ├── SimpleAgent.java     # Agent principal
│       │       ├── Main.java            # Point d'entrée
│       │       └── tools/
│       │           └── WeatherTool.java  # Outil personnalisé
│       └── resources/
│           └── application.properties
└── test/
    └── java/
        └── com/google/adk/samples/simpleagent/
            └── SimpleAgentTest.java
```

## Installation

### Prérequis

- Java 17+
- Maven 3.8+
- Clé API Google Gemini (AI Studio) ou compte Vertex AI

### Configuration

1. Cloner ou copier ce template
2. Installer les dépendances :
   ```bash
   mvn clean install
   ```

3. Configurer les variables d'environnement :
   ```bash
   cp .env.example .env
   # Éditer .env avec vos valeurs
   ```

## Utilisation

### Exécution locale

```java
import com.google.adk.agents.LlmAgent;
import com.google.adk.runner.InMemoryRunner;
import com.google.adk.sessions.Session;
import com.google.genai.types.Content;
import com.google.genai.types.Part;
import io.reactivex.rxjava3.core.Flowable;
import com.google.adk.events.Event;

// Créer l'agent
LlmAgent agent = SimpleAgent.create();

// Créer le runner
InMemoryRunner runner = new InMemoryRunner(agent, "simple_agent");

// Créer une session
Session session = runner.sessionService()
    .createSession("simple_agent", "user123", "session001")
    .blockingGet();

// Exécuter l'agent
Content userMessage = Content.fromParts(
    Part.fromText("Hello!")
);

Flowable<Event> events = runner.runAsync(
    "user123",
    session.id(),
    userMessage
);

// Traiter les événements
events.blockingForEach(event -> {
    if (event.finalResponse()) {
        System.out.println(event.stringifyContent());
    }
});
```

### Tests

```bash
mvn test
```

## Déploiement

### Build

```bash
mvn clean package
```

### Docker

```dockerfile
FROM openjdk:17-jdk-slim
WORKDIR /app
COPY target/simple-agent-*.jar app.jar
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]
```

## Fichiers clés

### src/main/java/.../SimpleAgent.java

```java
package com.google.adk.samples.simpleagent;

import com.google.adk.agents.LlmAgent;
import com.google.adk.samples.simpleagent.tools.WeatherTool;

public class SimpleAgent {
    public static LlmAgent create() {
        return LlmAgent.builder()
            .model("gemini-2.5-flash")
            .name("simple_agent")
            .description("Agent simple avec capacité météo")
            .instruction("""
                You are a helpful assistant that can provide weather information.
                When users ask about weather, use the get_weather tool.
                Be friendly and concise in your responses.
                """)
            .tools(WeatherTool.create())
            .build();
    }
}
```

### src/main/java/.../tools/WeatherTool.java

```java
package com.google.adk.samples.simpleagent.tools;

import com.google.adk.tools.FunctionTool;
import java.util.Map;

public class WeatherTool {
    public static FunctionTool create() {
        return FunctionTool.builder()
            .name("get_weather")
            .description("Get current weather for a city")
            .function((args) -> {
                String city = (String) args.get("city");
                String units = (String) args.getOrDefault("units", "celsius");
                
                // Mock implementation - replace with real API call
                return Map.of(
                    "status", "success",
                    "city", city,
                    "temperature", "25",
                    "units", units,
                    "condition", "sunny"
                );
            })
            .build();
    }
}
```

## Personnalisation

1. Modifier `SimpleAgent.java` pour définir votre agent
2. Ajouter des outils dans `tools/`
3. Adapter les instructions selon votre cas d'usage
4. Modifier les tests dans `test/`

## Ressources

- [Documentation ADK Java](../resources/04-api-reference.md)
- [Guide de démarrage](../resources/03-getting-started.md)
- [Agents.md](../../Agents.md) pour guide complet aux IA
