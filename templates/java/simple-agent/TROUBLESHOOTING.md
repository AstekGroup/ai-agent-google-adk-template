# Dépannage - Installation des dépendances Google ADK Java

## Problème identifié

Les dépendances Google ADK Java (`com.google.adk:adk` et `com.google.genai:genai`) ne sont **pas encore disponibles publiquement** dans Maven Central au moment de la rédaction de ce document.

### Erreur typique

```
[ERROR] Failed to execute goal on project simple-agent: Could not resolve dependencies
[ERROR] Could not find artifact com.google.adk:adk:jar:1.3.0 in central
[ERROR] Could not find artifact com.google.genai:genai:jar:1.3.0 in central
```

## Solutions possibles

### Solution 1 : Vérifier la disponibilité publique

Google ADK Java pourrait être disponible dans un repository public. Vérifiez :

1. **Repository GitHub officiel** : https://github.com/google/adk-java
   - Consultez la documentation pour les instructions d'installation
   - Vérifiez si des releases sont disponibles

2. **Documentation officielle** : https://google.github.io/adk-docs/
   - Section "Getting Started" pour Java
   - Instructions d'installation spécifiques

### Solution 2 : Installation depuis le code source

Si Google ADK Java est disponible uniquement en code source :

```bash
# Cloner le repository
git clone https://github.com/google/adk-java.git
cd adk-java

# Installer dans le repository local Maven
mvn clean install -DskipTests

# Répéter pour google-genai-java si nécessaire
git clone https://github.com/google/genai-java.git
cd genai-java
mvn clean install -DskipTests
```

### Solution 3 : Utiliser un repository Maven spécifique

Si Google fournit un repository Maven spécifique, ajoutez-le dans votre `pom.xml` :

```xml
<repositories>
    <repository>
        <id>google-adk-repo</id>
        <url>URL_DU_REPOSITORY_GOOGLE</url>
    </repository>
</repositories>
```

### Solution 4 : Installation manuelle des JARs

Si les JARs sont disponibles en téléchargement direct :

1. Téléchargez les JARs nécessaires
2. Installez-les dans votre repository local Maven :

```bash
mvn install:install-file \
  -Dfile=adk-1.3.0.jar \
  -DgroupId=com.google.adk \
  -DartifactId=adk \
  -Dversion=1.3.0 \
  -Dpackaging=jar

mvn install:install-file \
  -Dfile=genai-1.3.0.jar \
  -DgroupId=com.google.genai \
  -DartifactId=genai \
  -Dversion=1.3.0 \
  -Dpackaging=jar
```

### Solution 5 : Utiliser la version Python (temporairement)

En attendant que Google ADK Java soit disponible publiquement, vous pouvez :

- Utiliser la version Python du template (`templates/python/simple-agent/`)
- La version Python est disponible via `pip install google-adk`

## Vérifications à effectuer

1. **Vérifier la disponibilité** :
   ```bash
   # Chercher dans Maven Central
   curl https://search.maven.org/solrsearch/select?q=g:com.google.adk+AND+a:adk
   ```

2. **Vérifier le repository GitHub** :
   - Aller sur https://github.com/google/adk-java
   - Consulter les releases et la documentation
   - Vérifier les instructions d'installation dans le README

3. **Vérifier la documentation officielle** :
   - https://google.github.io/adk-docs/get-started/quickstart-java/
   - Instructions spécifiques pour Java

## Prochaines étapes

1. **Documenter** : Si vous trouvez la solution, documentez-la ici
2. **Mettre à jour** : Mettre à jour le `pom.xml` avec la bonne configuration
3. **Tester** : Une fois les dépendances installées, tester avec `mvn clean test`

## Ressources

- Repository GitHub : https://github.com/google/adk-java
- Documentation : https://google.github.io/adk-docs/
- Exemples : https://github.com/google/adk-samples
- Issues GitHub : https://github.com/google/adk-java/issues

## Note importante

Google ADK est un projet relativement récent. Il est possible que la version Java ne soit pas encore disponible publiquement dans Maven Central. Vérifiez régulièrement la disponibilité ou consultez les repositories GitHub officiels pour les dernières informations.

