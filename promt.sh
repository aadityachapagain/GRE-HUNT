#!/bin/bash

# make sure you gave a number of seconds:


description=$(cat <<-END
    Hello,

    I think its time you better revise the words in database or
    may be update database with new words.

    Bonjour !

END
)

while true; do
    python system_notify.py

    sleep $(( 3600*2 ))
done