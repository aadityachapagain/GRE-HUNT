import os 
import sys
import argparse

from core import insert

parser = argparse.ArgumentParser()

parser.add_argument("--append", 
                    help= 'append the word to database you just learned' , type= str)
parser.add_argument("--speech",
                    help= 'append speech to the word', type= str, default= '')
parser.add_argument('--meaning', 
                    help= 'meaning of the word to store in database', type= str)
parser.add_argument('--example', 
                    help= 'examples on how the given word can be used', default= '', nargs='?')
parser.add_argument('--usage', 
                    help= 'usage example of words in different context', default= '', nargs='?')

parser.add_argument('--list', type= int, 
                    help= 'return few words revised or  added in last few hours')
parser.add_argument('--list-all', type = int, 
                    help= 'return few words in last all the words in 24 hrs')


args = parser.parse_args()

print(args)

if args.append:
    insert(args.append, args.speech ,args.meaning, args.example, args.usage)

if args.list:
    print('listing is in progress . . . ')
    print('list of last few words are . . . .')