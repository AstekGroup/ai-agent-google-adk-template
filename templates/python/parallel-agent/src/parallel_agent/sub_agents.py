"""Agents de recherche parallèle et agent de fusion."""

from google.adk.agents import Agent

# Researcher 1 : Recherche sur les énergies renouvelables
researcher_1 = Agent(
    model="gemini-2.5-flash",
    name="renewable_energy_researcher",
    description="Recherche sur les énergies renouvelables",
    instruction="""You are a researcher specializing in renewable energy.

Research topic: renewable energy sources and latest trends

Your task:
1. Research the latest developments in renewable energy
2. Focus on solar, wind, and hydroelectric power
3. Summarize key findings concisely (2-3 sentences)
4. Output only the summary, no meta-commentary""",
    output_key="renewable_energy_result"
)

# Researcher 2 : Recherche sur les véhicules électriques
researcher_2 = Agent(
    model="gemini-2.5-flash",
    name="ev_researcher",
    description="Recherche sur les véhicules électriques",
    instruction="""You are a researcher specializing in electric vehicles.

Research topic: electric vehicle technology and market trends

Your task:
1. Research the latest developments in EV technology
2. Focus on battery technology, charging infrastructure, and market adoption
3. Summarize key findings concisely (2-3 sentences)
4. Output only the summary, no meta-commentary""",
    output_key="ev_technology_result"
)

# Researcher 3 : Recherche sur la capture de carbone
researcher_3 = Agent(
    model="gemini-2.5-flash",
    name="carbon_capture_researcher",
    description="Recherche sur la capture de carbone",
    instruction="""You are a researcher specializing in carbon capture.

Research topic: carbon capture and storage methods

Your task:
1. Research current carbon capture technologies
2. Focus on effectiveness, costs, and scalability
3. Summarize key findings concisely (2-3 sentences)
4. Output only the summary, no meta-commentary""",
    output_key="carbon_capture_result"
)

# Merger Agent : Fusionne les résultats de recherche
merger_agent = Agent(
    model="gemini-2.5-pro",
    name="synthesis_agent",
    description="Synthétise les résultats de recherche parallèle",
    instruction="""You are a synthesis specialist.

Your task:
1. Review the research results from parallel researchers:
   - Renewable Energy: {renewable_energy_result}
   - Electric Vehicles: {ev_technology_result}
   - Carbon Capture: {carbon_capture_result}

2. Synthesize these findings into a coherent report

3. Structure your response with:
   - Introduction
   - Key findings from each area
   - Connections and relationships between findings
   - Conclusion

Be comprehensive but concise.""",
    output_key="synthesis_report"
)
