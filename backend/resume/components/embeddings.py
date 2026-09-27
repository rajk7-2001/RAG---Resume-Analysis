from sentence_transformers import SentenceTransformer
import faiss
from .helperfunc import timer

embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

@timer
def perform_text_embedding(chunks):
    embeddings = embedding_model.encode(chunks).astype('float32')
    faiss.normalize_L2(embeddings)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  
    index.add(embeddings)
    return index

@timer    
def perform_query_embeddings(query):
    embeddings = embedding_model.encode([query]).astype('float32')
    faiss.normalize_L2(embeddings)
    return embeddings

@timer    
def perfrom_similarity_search(text_index, query_embeddings):
    scores, indices = text_index.search(query_embeddings, k=5)
    return scores, indices
    
    
    
    