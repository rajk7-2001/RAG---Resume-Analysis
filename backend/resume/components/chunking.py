from langchain_text_splitters import RecursiveCharacterTextSplitter
from .helperfunc import timer

@timer
def chunking(normalized_text):
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 200,
        chunk_overlap = 20
    )
    
    chunks = splitter.split_text(normalized_text)
    return chunks
