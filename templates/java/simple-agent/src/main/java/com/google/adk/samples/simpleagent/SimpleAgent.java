package com.google.adk.samples.simpleagent;

import com.google.adk.agents.LlmAgent;
import com.google.adk.samples.simpleagent.tools.WeatherTool;

/**
 * Agent principal simple avec capacité météo.
 * 
 * Cet agent démontre comment créer un agent Google ADK de base avec un outil personnalisé.
 */
public class SimpleAgent {
    
    /**
     * Crée et configure l'agent simple avec l'outil météo.
     * 
     * @return LlmAgent configuré avec l'outil météo
     */
    public static LlmAgent create() {
        return LlmAgent.builder()
            .model("gemini-2.5-flash")
            .name("simple_agent")
            .description("Agent simple avec capacité de fournir des informations météo")
            .instruction("""
                You are a helpful assistant that can provide weather information.

                When users ask about the weather:
                1. Identify the city name from their query
                2. Use the get_weather tool to retrieve weather information
                3. Present the information in a friendly and clear manner

                Be concise and helpful. If you don't have weather information for a city, 
                apologize and suggest checking a weather service directly.
                """)
            .tools(WeatherTool.create())
            .build();
    }
}

