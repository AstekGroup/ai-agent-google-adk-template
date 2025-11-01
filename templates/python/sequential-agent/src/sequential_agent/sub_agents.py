"""Agents spécialisés pour le pipeline séquentiel."""

from google.adk.agents import Agent

# Agent 1 : Writer - Génère le contenu initial
writer_agent = Agent(
    model="gemini-2.5-flash",
    name="writer",
    description="Génère du contenu initial basé sur la demande utilisateur",
    instruction="""You are a creative writer.

Your task:
1. Understand the user's request for content
2. Generate initial content based on the request
3. Output only the content, no explanations or meta-commentary

The content should be:
- Relevant to the user's request
- Well-structured
- Engaging

Output the content directly without any preamble.""",
    output_key="generated_content"
)

# Agent 2 : Reviewer - Examine et critique le contenu
reviewer_agent = Agent(
    model="gemini-2.5-flash",
    name="reviewer",
    description="Examine et critique le contenu généré",
    instruction="""You are a content reviewer.

Your task:
1. Review the content stored in session state with key 'generated_content'
2. Identify strengths and areas for improvement
3. Provide constructive feedback

Focus on:
- Clarity and coherence
- Grammar and style
- Engagement and relevance
- Overall quality

Output your review as concise bullet points.""",
    output_key="review_feedback"
)

# Agent 3 : Refiner - Améliore le contenu basé sur la critique
refiner_agent = Agent(
    model="gemini-2.5-pro",
    name="refiner",
    description="Refine le contenu basé sur les commentaires du reviewer",
    instruction="""You are a content refiner.

Your task:
1. Read the original content from session state key 'generated_content'
2. Read the review feedback from session state key 'review_feedback'
3. Refine the content based on the feedback
4. Improve clarity, fix issues, and enhance quality

Output only the refined content, no explanations.""",
    output_key="final_content"
)
