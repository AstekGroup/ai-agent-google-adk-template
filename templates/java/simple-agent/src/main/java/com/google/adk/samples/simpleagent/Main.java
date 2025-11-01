package com.google.adk.samples.simpleagent;

import com.google.adk.agents.LlmAgent;
import com.google.adk.runner.InMemoryRunner;
import com.google.adk.sessions.Session;
import com.google.genai.types.Content;
import com.google.genai.types.Part;
import io.reactivex.rxjava3.core.Flowable;
import com.google.adk.events.Event;

/**
 * Point d'entrée principal pour l'agent simple.
 * 
 * Cet exemple montre comment :
 * - Créer un agent
 * - Créer un runner avec gestion de session
 * - Exécuter l'agent avec un message utilisateur
 * - Traiter les événements retournés
 */
public class Main {
    
    public static void main(String[] args) {
        // Créer l'agent
        LlmAgent agent = SimpleAgent.create();
        
        // Créer le runner
        InMemoryRunner runner = new InMemoryRunner(agent, "simple_agent");
        
        // Créer une session
        Session session = runner.sessionService()
            .createSession("simple_agent", "user123", "session001")
            .blockingGet();
        
        // Exécuter l'agent avec un message utilisateur
        Content userMessage = Content.fromParts(
            Part.fromText("What's the weather in Paris?")
        );
        
        Flowable<Event> events = runner.runAsync(
            "user123",
            session.id(),
            userMessage
        );
        
        // Traiter les événements
        System.out.println("=== Réponses de l'agent ===\n");
        events.blockingForEach(event -> {
            if (event.finalResponse()) {
                System.out.println(event.stringifyContent());
            } else if (event.toolCall() != null) {
                System.out.println("Tool call: " + event.toolCall().name());
            }
        });
    }
}

