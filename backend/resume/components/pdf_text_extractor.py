from pypdf import PdfReader
import sys
from .helperfunc import timer

sys.stdout.reconfigure(encoding="utf-8")

@timer
def pdf_extractor(pdf_file):
    
    reader = PdfReader(pdf_file)
    
    text = ""
    
    for page in reader.pages:
        page_text = page.extract_text()
        
        if page_text:
            text += page_text + "\n"
                
    return text
            
