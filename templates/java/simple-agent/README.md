# Simple Agent Template - Java

Agent Google ADK simple avec un outil de météo en Java.

## Prérequis

- Java 17+
- Maven 3.8+
- Clé API Google Gemini (AI Studio) ou compte Vertex AI

## Installation

### ⚠️ Note importante sur les dépendances

**Les dépendances Google ADK Java ne sont pas encore disponibles publiquement dans Maven Central.**

Si vous rencontrez des erreurs lors de l'installation des dépendances (`Could not find artifact com.google.adk:adk:jar:1.3.0`), consultez le fichier **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** pour les solutions possibles.

### Installation des dépendances

```bash
# Installer les dépendances
mvn clean install
```

**Si l'installation échoue**, suivez les instructions dans [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Configuration

```bash
# Copier le fichier d'exemple de variables d'environnement
cp .env.example .env
# Éditer .env avec vos valeurs
```

Assurez-vous de définir `GOOGLE_API_KEY` dans votre environnement ou dans `.env`:

```bash
export GOOGLE_API_KEY=your-api-key-here
```

## Utilisation

### Exécution locale

```bash
# Compiler le projet
mvn clean package

# Exécuter l'application
java -jar target/simple-agent-1.0.0.jar
```

### Utilisation programmatique

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
    Part.fromText("What's the weather in Paris?")
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

## Tests

```bash
# Exécuter tous les tests
mvn test

# Exécuter un test spécifique
mvn test -Dtest=SimpleAgentTest
```

## Structure du projet

```
simple-agent/
├── pom.xml                              # Configuration Maven
├── README.md                            # Ce fichier
├── .env.example                         # Exemple de variables d'environnement
├── .gitignore                           # Fichiers ignorés par Git
├── src/
│   └── main/
│       ├── java/
│       │   └── com/google/adk/samples/simpleagent/
│       │       ├── SimpleAgent.java     # Agent principal
│       │       ├── Main.java            # Point d'entrée
│       │       └── tools/
│       │           └── WeatherTool.java # Outil météo
│       └── resources/
│           └── application.properties   # Configuration
└── src/
    └── test/
        └── java/
            └── com/google/adk/samples/simpleagent/
                └── SimpleAgentTest.java  # Tests unitaires
```

## Personnalisation

### Modifier l'agent

Éditez `src/main/java/com/google/adk/samples/simpleagent/SimpleAgent.java` pour :
- Changer le modèle LLM
- Modifier les instructions système
- Ajouter ou retirer des outils

### Ajouter un outil

1. Créez une nouvelle classe dans `src/main/java/com/google/adk/samples/simpleagent/tools/`
2. Implémentez `FunctionTool` selon le pattern de `WeatherTool`
3. Ajoutez l'outil à l'agent dans `SimpleAgent.create()`

Exemple :

```java
public class MyCustomTool {
    public static FunctionTool create() {
        return FunctionTool.builder()
            .name("my_tool")
            .description("Description de mon outil")
            .functionSchema(...)
            .function(args -> {
                // Implémentation
                return Map.of("result", "value");
            })
            .build();
    }
}
```

## Déploiement

### Build JAR

```bash
mvn clean package
```

Le JAR sera créé dans `target/simple-agent-1.0.0.jar`

### Docker

Créez un `Dockerfile` :

```dockerfile
FROM openjdk:17-jdk-slim
WORKDIR /app
COPY target/simple-agent-*.jar app.jar
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]
```

Build et exécution :

```bash
docker build -t simple-agent .
docker run -p 8080:8080 -e GOOGLE_API_KEY=your-key simple-agent
```

### Vertex AI Agent Engine

Pour déployer sur Vertex AI Agent Engine, référez-vous à la documentation dans `resources/06-deployment.md`.

## Ressources

- [Documentation ADK Java](../../../resources/04-api-reference.md)
- [Guide de démarrage](../../../resources/03-getting-started.md)
- [Agents.md](../../../Agents.md) pour guide complet aux IA
- [Exemples et patterns](../../../resources/05-examples-patterns.md)

## Notes

- L'outil météo utilise des données mockées pour démonstration. Remplacez par un appel API réel vers un service météo (OpenWeatherMap, WeatherAPI, etc.).
- Assurez-vous de configurer correctement vos variables d'environnement avant l'exécution.
- Pour la production, utilisez Vertex AI au lieu d'AI Studio.

## Licence

Ce template est fourni à des fins éducatives et de développement. Consultez les licences des projets Google ADK pour plus d'informations.

