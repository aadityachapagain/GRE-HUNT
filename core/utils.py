import re

from datetime import datetime


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