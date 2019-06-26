import re
from typing import Dict

from datetime import datetime, timedelta


def detokenize(val):
    '''
    function to remove "_" from words and
    detokenize the words to represent correct 
    word'''

    return ' '.join(re.split('[_]+',val.strip()))

def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M')

def tokenize(val):
    return re.split('[_]+',val.strip())

def get_date_from_string(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d %H:%M')

def get_time_diff(delta):
    return timedelta(days=delta)


def display_format(doc: Dict):
    info = ''

    info += f"\n\t word:  {doc['word']}\n"

    if doc['speech']:
        info += f'\n\t speech: {doc["speech"]}\n'
    
    info += f'\n\t meaning: {doc["meaning"]}\n'
    
    if doc['usage'].strip():
        info += f'\n\t example: {doc["usage"]}\n'

    if doc['example'].strip():
        info += f'\n\t Synonyms: {doc["example"]}\n'

    return info