import os 
import sys
from core import insert

argument = sys.argv[1]

if argument == 'append':
    print(sys.argv[2:])
    # insert(sys.argv[2], ' '.join(sys.argv[3:]))
elif argument == 'list':
    pass
elif argument == 'list-all':
    pass