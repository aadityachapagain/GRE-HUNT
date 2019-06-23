from .db import db
from core.utils import detokenize, current_time

def insert(word : str, meaning : str, usage = '', example = ''):
    doc = {'word':detokenize(word), 'meaning': detokenize(meaning), 'example':detokenize(example),
            'usage':detokenize(usage), 'date':current_time()}

    print(doc)