"""
Title: Weaviate Quickstart Collection
Author: Ann Hagan - copied from Weaviate documentationhttps://weaviate.io/developers/weaviate/quickstart/local
Date: 2024
Purpose: creates a simple retrieval augmented generation (RAG) query based on the text embeddings.
"""

import weaviate

client = weaviate.connect_to_local()

questions = client.collections.get("Question")

response = questions.generate.near_text(
    query="biology",
    limit =2,
    grouped_task="Write a tweet with emojis about these facts."
)

print(response.generated)

client.close()  # Free up resources