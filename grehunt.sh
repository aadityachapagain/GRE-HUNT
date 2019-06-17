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
    case $1 in
        -a | --append  ) shift
                         python app.py append $1
                         ;;

        list            ) shift
                         python app.py list $1

        list-all        ) shift
                         python app.py list-all $1
else
    usage
fi