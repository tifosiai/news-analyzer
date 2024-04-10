from stemming import stem_sentence
from utils import load_pos_model

class Stemmer:
    def __init__(self):
        self.model, self.w2i, self.idx2tag = load_pos_model()
    
    def stem(self, text):
        stemmed_sentence = stem_sentence(text, self.model, self.w2i, self.idx2tag)
        return stemmed_sentence