FROM openjdk:17-jdk-slim

WORKDIR /app

# Copier le JAR construit
COPY target/simple-agent-*.jar app.jar

# Exposer le port (si vous ajoutez un serveur HTTP plus tard)
EXPOSE 8080

# Variables d'environnement par défaut
ENV GOOGLE_GENAI_USE_VERTEXAI=0
ENV APP_NAME=simple_agent
ENV LOG_LEVEL=INFO

# Exécuter l'application
CMD ["java", "-jar", "app.jar"]

