from .db import db

def insert(word : str, meaning : str, usage = '', example = ''):
    print(word, '  ', meaning)