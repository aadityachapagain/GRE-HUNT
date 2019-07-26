#!/usr/bin/env python3

from app.core import get_random_record, display_to_shell_extension

print('Vocab-It')
print('\n---')

for doc in get_random_record(5):
    display_to_shell_extension(doc)