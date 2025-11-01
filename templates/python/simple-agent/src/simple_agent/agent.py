"""Agent principal simple avec capacité météo."""

from google.adk.agents import Agent
from .tools import get_weather_tool

root_agent = Agent(
    model="gemini-2.5-flash",
    name="simple_agent",
    description="Agent simple avec capacité de fournir des informations météo",
    instruction="""You are a helpful assistant that can provide weather information.

When users ask about the weather:
1. Identify the city name from their query
2. Use the get_weather tool to retrieve weather information
3. Present the information in a friendly and clear manner

Be concise and helpful. If you don't have weather information for a city, apologize and suggest checking a weather service directly.""",
    tools=[get_weather_tool]
)
