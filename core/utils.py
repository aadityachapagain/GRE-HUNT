
from datetime import datetime


def detokenize(val):
    '''
    function to remove "_" from words and
    detokenize the words to represent correct 
    word'''

    return val.replace('_',' ')

def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M')