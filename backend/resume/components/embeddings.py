import os
import numpy as np
import faiss

from google import genai
from google.genai import types

from .helperfunc import timer
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


@timer
def perform_text_embedding(chunks):

    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=chunks,
        config=types.EmbedContentConfig(
            output_dimensionality=768
        )
    )

    embeddings = np.array(
        [embedding.values for embedding in result.embeddings],
        dtype="float32"
    )

    faiss.normalize_L2(embeddings)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    return index


@timer
def perform_query_embeddings(query):

    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=[query],
        config=types.EmbedContentConfig(
            output_dimensionality=768
        )
    )

    embeddings = np.array(
        [embedding.values for embedding in result.embeddings],
        dtype="float32"
    )

    faiss.normalize_L2(embeddings)

    return embeddings


@timer
def perfrom_similarity_search(text_index, query_embeddings):

    scores, indices = text_index.search(
        query_embeddings,
        k=5
    )

    return scores, indices