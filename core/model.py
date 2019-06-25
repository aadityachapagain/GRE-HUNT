from core.db import vocab
from core.utils import detokenize, current_time, tokenize, get_date_from_string, get_time_diff

def insert(word : str, speech: str,meaning : str, usage = '', example = ''):
    doc = {'word':detokenize(word), 'speech':tokenize(speech),'meaning': detokenize(meaning), 'example':detokenize(example),
            'usage':detokenize(usage), 'date':current_time()}

    vocab.insert_one(doc)

def display(timestamp):
        items = []
        last_time = get_date_from_string(current_time()) - get_time_diff(timestamp)
        for docs in vocab.find({},{'_id':0}).limit(100):
                if get_date_from_string(docs['date']) > last_time:
                        items.append(docs)
        
        return docs