"""
Title: Weaviate Quickstart Collection
Author: Ann Hagan - copied from Weaviate documentationhttps://weaviate.io/developers/weaviate/quickstart/local
Date: 2024
Purpose: Creates a connection to Weaviate via Docker. Instantiates a schema for the collection called Question.
"""

import weaviate
from weaviate.classes.config import Configure

client = weaviate.connect_to_local()

print(client.is_ready())



#Generates a collection
#The following example creates a collection called Question with:

#Ollama embedding model integration to create vectors during ingestion & queries, using the nomic-embed-text model, and
#Ollama generative AI integrations for retrieval augmented generation (RAG), using the llama3.2 model.

questions = client.collections.create(
    name="Question",
    vectorizer_config=Configure.Vectorizer.text2vec_ollama(     # Configure the Ollama embedding integration
        api_endpoint="http://host.docker.internal:11434",       # Allow Weaviate from within a Docker container to contact your Ollama instance
        model="nomic-embed-text",                               # The model to use
    ),
    generative_config=Configure.Generative.ollama(              # Configure the Ollama generative integration
        api_endpoint="http://host.docker.internal:11434",       # Allow Weaviate from within a Docker container to contact your Ollama instance
        model="llama3.2",                                       # The model to use
    )
)

client.close()  # Free up resources