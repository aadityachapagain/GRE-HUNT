from core.db import vocab
from core.utils import detokenize, current_time, tokenize

def insert(word : str, speech: str,meaning : str, usage = '', example = ''):
    doc = {'word':detokenize(word), 'speech':tokenize(speech),'meaning': detokenize(meaning), 'example':detokenize(example),
            'usage':detokenize(usage), 'date':current_time()}

    vocab.insert_one(doc)

def display(timestamp):
        pass