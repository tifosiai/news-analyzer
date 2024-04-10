from stemming import stem_sentence
from utils import load_pos_model, pos_tag_predict


text = "Salam mənim adım İlqardı"

def convert_to_stemmed(text):
    # Load the model
    model, w2i, idx2tag = load_pos_model()
    return stem_sentence(text, model, w2i, idx2tag)        
    

print(convert_to_stemmed(text))