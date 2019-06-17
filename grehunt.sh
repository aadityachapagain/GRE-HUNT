#!/bin/bash

# press enter to continue
# echo -en "\n Press Enter to continue"

usage()
{
    echo "  usage [options] <arguments>

        options:
        
        -a , --append       : append the word into word database
        list                : list few last words added to the database
        list-all            : list all the words added to the database
     "

}

if [ $# -gt 0 ]; then
    echo "Your command line contains $# arguments"
else
    usage
fi