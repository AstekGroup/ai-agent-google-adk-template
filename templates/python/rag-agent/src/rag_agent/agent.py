"""Agent avec RAG Vertex AI pour recherche contextuelle."""

import os
from google.adk.agents import Agent
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag

# Récupérer le corpus RAG depuis les variables d'environnement
rag_corpus = os.getenv("RAG_CORPUS")

if not rag_corpus:
    raise ValueError(
        "RAG_CORPUS environment variable must be set. "
        "Format: projects/PROJECT_ID/locations/LOCATION/ragCorpora/CORPUS_ID"
    )

# Créer l'outil RAG
rag_retrieval_tool = VertexAiRagRetrieval(
    name='retrieve_documentation',
    description='Retrieve relevant documentation and reference materials from the RAG corpus',
    rag_resources=[
        rag.RagResource(rag_corpus=rag_corpus)
    ],
    similarity_top_k=10,
    vector_distance_threshold=0.6,
)

# Créer l'agent avec RAG
root_agent = Agent(
    model='gemini-2.5-flash',
    name='rag_agent',
    description='Agent de documentation avec recherche RAG',
    instruction="""You are a documentation assistant powered by RAG (Retrieval-Augmented Generation).

Your capabilities:
1. Answer questions using information from the RAG corpus
2. Retrieve relevant documentation using the retrieve_documentation tool
3. Provide accurate answers with proper citations
4. Acknowledge when information is not available in the corpus

Guidelines:
- Always use the retrieve_documentation tool when answering questions
- Cite your sources when referencing retrieved information
- If information is not found, clearly state that
- Be concise but comprehensive in your answers""",
    tools=[rag_retrieval_tool]
)
