import sys
import contractions
import re 
import spacy
from .helperfunc import timer

sys.stdout.reconfigure(encoding='utf-8')

@timer
class TextNormalization:
    def __init__(self,text):
        self.data = text
    
    def lowercase(self):
        self.data = self.data.lower()
    
    def extra_spaces_remover(self):
        splitted_data = self.data.split()
        removed_space = ' '.join(splitted_data)
        self.data = removed_space
    
    def expanding_sform(self):
        self.data = contractions.fix(self.data)
    
    def remove_spl_char(self):
        self.data = re.sub("[^A-Za-z .,:()]",'',self.data)
        
    def spacy_text(self):
        nlp = spacy.load('en_core_web_sm')
        processed_text = nlp(self.data)
        modified_words = [token.lemma_ for token in processed_text if not token.is_stop]
        self.data = ' '.join(modified_words)
             
    def execution(self):
        self.lowercase()
        self.extra_spaces_remover()
        self.expanding_sform()
        self.remove_spl_char()
        self.spacy_text()
        return self.data
    
      
