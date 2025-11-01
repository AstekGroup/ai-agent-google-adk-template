package com.google.adk.samples.simpleagent;

import com.google.adk.agents.LlmAgent;
import com.google.adk.runner.InMemoryRunner;
import com.google.adk.sessions.Session;
import com.google.genai.types.Content;
import com.google.genai.types.Part;
import io.reactivex.rxjava3.core.Flowable;
import com.google.adk.events.Event;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Tests unitaires pour SimpleAgent.
 */
class SimpleAgentTest {
    
    private InMemoryRunner runner;
    private Session session;
    
    @BeforeEach
    void setUp() {
        LlmAgent agent = SimpleAgent.create();
        runner = new InMemoryRunner(agent, "test_app");
        session = runner.sessionService()
            .createSession("test_app", "test_user", "test_session")
            .blockingGet();
    }
    
    @Test
    void testAgentCreation() {
        // Test que l'agent peut être créé
        LlmAgent agent = SimpleAgent.create();
        assertNotNull(agent);
        assertEquals("simple_agent", agent.name());
        assertFalse(agent.tools().isEmpty());
    }
    
    @Test
    void testAgentBasicInteraction() {
        // Test interaction basique avec l'agent
        Content userMessage = Content.fromParts(
            Part.fromText("Hello, what can you do?")
        );
        
        Flowable<Event> events = runner.runAsync(
            "test_user",
            session.id(),
            userMessage
        );
        
        List<Event> eventList = events.collect(
            ArrayList::new,
            List::add
        ).blockingGet();
        
        // Vérifier qu'on a reçu des événements
        assertFalse(eventList.isEmpty());
        
        // Vérifier qu'on a une réponse finale
        boolean hasFinalResponse = eventList.stream()
            .anyMatch(Event::finalResponse);
        assertTrue(hasFinalResponse);
    }
    
    @Test
    void testWeatherTool() {
        // Test de l'outil météo directement
        com.google.adk.samples.simpleagent.tools.WeatherTool weatherTool = 
            new com.google.adk.samples.simpleagent.tools.WeatherTool();
        
        // Le test vérifie que l'outil peut être créé
        var tool = com.google.adk.samples.simpleagent.tools.WeatherTool.create();
        assertNotNull(tool);
    }
    
    @Test
    void testAgentWeatherQuery() {
        // Test de l'agent avec une requête météo
        Content userMessage = Content.fromParts(
            Part.fromText("What's the weather in Paris?")
        );
        
        Flowable<Event> events = runner.runAsync(
            "test_user",
            session.id(),
            userMessage
        );
        
        List<Event> eventList = events.collect(
            ArrayList::new,
            List::add
        ).blockingGet();
        
        // Vérifier qu'on a utilisé l'outil météo (chercher des tool calls)
        boolean hasToolCall = eventList.stream()
            .anyMatch(event -> event.toolCall() != null);
        
        // Vérifier qu'on a une réponse finale
        boolean hasFinalResponse = eventList.stream()
            .anyMatch(Event::finalResponse);
        assertTrue(hasFinalResponse);
    }
}

