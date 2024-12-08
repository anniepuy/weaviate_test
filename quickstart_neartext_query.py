"""
Title: Weaviate Quickstart Collection
Author: Ann Hagan - copied from Weaviate documentationhttps://weaviate.io/developers/weaviate/quickstart/local
Date: 2024
Purpose: Imports a simple near text sear based on the text embeddings.
"""
import weaviate
import json

client = weaviate.connect_to_local()

questions = client.collections.get("Question")

response = questions.query.near_text(
    query="biology",
    limit =2
)

for obj in response.objects:
    print(json.dumps(obj.properties, indent=2))

client.close()