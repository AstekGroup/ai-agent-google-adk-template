"""Sous-agents pour l'agent personnalisé."""

from google.adk.agents import LlmAgent

# Générator d'histoire
story_generator = LlmAgent(
    name="StoryGenerator",
    model="gemini-2.5-flash",
    description="Génère l'histoire initiale",
    instruction="""Write a short story (around 100 words) on the topic provided in session state with key 'topic'""",
    output_key="current_story"
)

# Critique
critic = LlmAgent(
    name="Critic",
    model="gemini-2.5-flash",
    description="Critique l'histoire",
    instruction="""Review the story provided in session state with key 'current_story'. 
    Provide 1-2 sentences of constructive criticism on how to improve it. Focus on plot or character.""",
    output_key="criticism"
)

# Réviseur
reviser = LlmAgent(
    name="Reviser",
    model="gemini-2.5-flash",
    description="Révise l'histoire basé sur la critique",
    instruction="""Revise the story provided in session state with key 'current_story', 
    based on the criticism in session state with key 'criticism'. Output only the revised story.""",
    output_key="current_story"
)

# Vérification grammaire
grammar_check = LlmAgent(
    name="GrammarCheck",
    model="gemini-2.5-flash",
    description="Vérifie la grammaire",
    instruction="""Check the grammar of the story provided in session state with key 'current_story'. 
    Output only the suggested corrections as a list, or output 'Grammar is good!' if there are no errors.""",
    output_key="grammar_suggestions"
)

# Vérification du ton
tone_check = LlmAgent(
    name="ToneCheck",
    model="gemini-2.5-flash",
    description="Analyse le ton de l'histoire",
    instruction="""Analyze the tone of the story provided in session state with key 'current_story'. 
    Output only one word: 'positive' if the tone is generally positive, 'negative' if generally negative, or 'neutral' otherwise.""",
    output_key="tone_check_result"
)
