import os 
import sys
import argparse

from core import insert

parser = argparse.ArgumentParser()

parser.add_argument("--append", 
                    help= 'append the word to database you just learned' , type= str)
parser.add_argument('--meaning', 
                    help= 'meaning of the word to store in database',)
parser.add_argument('--example', 
                    help= 'examples on how the given word can be used', default= '', nargs='?')
parser.add_argument('--usage', 
                    help= 'usage example of words in different context', default= '', nargs='?')

parser.add_argument('--list')
parser.add_argument('--list-all')

print(parser.parse_args())

print(sys.argv)