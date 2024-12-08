"""
Title: Weaviate Quickstart Collection
Author: Ann Hagan - copied from Weaviate documentationhttps://weaviate.io/developers/weaviate/quickstart/local
Date: 2024
Purpose: Imports data to the Question collection.
"""
import weaviate
import requests, json

client = weaviate.connect_to_local()

resp = requests.get(
    "https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json"
)
data = json.loads(resp.text)

questions = client.collections.get("Question")

with questions.batch.dynamic() as batch:
    for d in data:
        batch.add_object({
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"],
        })

client.close()  # Free up resources