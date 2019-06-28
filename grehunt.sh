#!/bin/bash

# press enter to continue
# echo -en "\n Press Enter to continue"

# Author: Aaditya Chapagain
# Project: Gre-HUNT
# version: 0.1.1

usage()
{
    echo <<EOF
      usage [options] <arguments>

        options:
        
        -a , --append           : append the word into word database
        list    [num]           : list few last words added to the database
        list-all                : list all the words added to the database
        random  [num]           : list random words from database
EOF
}

wrong_command()
{
    echo " Unknown options !
            
            provide --help or -h to see command usage
            "
}

append_usage()
{
    cat <<EOF 

    usage:
    --apend usage pattern 
    
            [--append | -a ] <Word>  [--speech <speech>] <meaning> [optional] --example  <write all the example of using given word>
             --usage <write the synonyms or use of word in manykind>

EOF
}
/
operations()
{
    local ops="$1"
    shift
    if [ $# -gt 0 ]; then
        python app.py "$ops" $1
    else
        usage
        exit
    fi
}

if [ $# -gt 0 ]; then
    case $1 in
        -a | --append )  shift
                         if [ $# -gt 0 ]; then

                            arg1="${1// /_}"
                         else
                            append_usage
                            exit
                         fi
                         shift
                        if [ "$1" == "--speech" ]; then
                            shift
                            speech="${1// /_}"
                        else
                            speech="__"
                        fi
                        shift
                         if [ $# -gt 0 ]; then
                            arg2="${1// /_}"
                         else
                            append_usage
                            exit
                         fi

                         shift

                         if [ "$1" == "--example" ]; then
                            shift
                            arg3="${1// /_}"
                            shift
                            if [ "$1" == "--usage" ]; then
                                shift
                                arg4="${1// /_}"
                                shift
                                if [ $# -gt 0 ]; then
                                    append_usage
                                fi
                                python app.py --append $arg1 --speech $speech --meaning $arg2 --example $arg3 --usage $arg4
                             else
                                 python app.py --append $arg1 --speech $speech --meaning $arg2 --example $arg3
                            fi

                         else
                            python app.py --append $arg1 --speech $speech --meaning $arg2
                         fi
                         ;;

        list )           shift
                         operations "--list" "$1"
                         ;;

        list-all )       shift
                         operations "--list-all" "$1"
                         ;;

        random )         shift
                          operations "--random" "$1"
                          ;;

        --help | -h )    usage
                         ;;
        * )              wrong_command
                         
    esac
else
    usage
fi