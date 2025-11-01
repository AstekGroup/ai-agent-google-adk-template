package com.google.adk.samples.simpleagent.tools;

import com.google.adk.tools.FunctionTool;
import java.util.Map;
import java.util.HashMap;

/**
 * Outil météo pour l'agent simple.
 * 
 * Cet outil démontre comment créer un FunctionTool personnalisé en Java.
 * Note: Cette implémentation est un mock. Remplacez par un appel API réel 
 * vers un service météo (OpenWeatherMap, WeatherAPI, etc.).
 */
public class WeatherTool {
    
    // Données mock pour démonstration
    private static final Map<String, WeatherData> MOCK_DATA = new HashMap<>();
    
    static {
        MOCK_DATA.put("paris", new WeatherData(15, "cloudy"));
        MOCK_DATA.put("london", new WeatherData(12, "rainy"));
        MOCK_DATA.put("new york", new WeatherData(20, "sunny"));
        MOCK_DATA.put("tokyo", new WeatherData(18, "partly cloudy"));
    }
    
    /**
     * Crée l'outil FunctionTool pour récupérer la météo.
     * 
     * @return FunctionTool configuré pour get_weather
     */
    public static FunctionTool create() {
        return FunctionTool.builder()
            .name("get_weather")
            .description("Get current weather information for a city. " +
                        "This is a mock implementation. Replace with actual API call to a weather service.")
            .functionSchema(Map.of(
                "type", "object",
                "properties", Map.of(
                    "city", Map.of(
                        "type", "string",
                        "description", "The name of the city"
                    ),
                    "units", Map.of(
                        "type", "string",
                        "enum", new String[]{"celsius", "fahrenheit"},
                        "description", "Temperature units (celsius or fahrenheit)",
                        "default", "celsius"
                    )
                ),
                "required", new String[]{"city"}
            ))
            .function(args -> {
                String city = (String) args.get("city");
                String units = (String) args.getOrDefault("units", "celsius");
                
                String cityLower = city != null ? city.toLowerCase() : "";
                WeatherData data = MOCK_DATA.get(cityLower);
                
                Map<String, Object> result = new HashMap<>();
                
                if (data != null) {
                    double temp = data.temperature;
                    if ("fahrenheit".equals(units)) {
                        temp = (temp * 9.0 / 5.0) + 32;
                    }
                    
                    result.put("status", "success");
                    result.put("city", city);
                    result.put("temperature", String.valueOf(temp));
                    result.put("units", units);
                    result.put("condition", data.condition);
                } else {
                    result.put("status", "error");
                    result.put("city", city);
                    result.put("message", 
                        String.format("Weather information not available for %s", city));
                }
                
                return result;
            })
            .build();
    }
    
    /**
     * Classe interne pour stocker les données météo mockées.
     */
    private static class WeatherData {
        final int temperature;
        final String condition;
        
        WeatherData(int temperature, String condition) {
            this.temperature = temperature;
            this.condition = condition;
        }
    }
}

