from .textnormalization import TextNormalization
from .chunking import chunking
from .embeddings import perform_text_embedding, perform_query_embeddings, perfrom_similarity_search
from .llm import generation

def execution(text,query):
    normalized_text_obj = TextNormalization(text)
    normalized_text = normalized_text_obj.execution() 
    chunked_text = chunking(normalized_text)
    embedding_data = perform_text_embedding(chunked_text)
    normalized_query_obj = TextNormalization(query)
    normalized_query_text = normalized_query_obj.execution()
    query_embeddings = perform_query_embeddings(normalized_query_text)
    scores,similar_indices = perfrom_similarity_search(embedding_data,query_embeddings)
    retrieved_chunks = [chunked_text[i] for i in similar_indices[0]]
    final_response = generation(query,retrieved_chunks)
    return final_response
