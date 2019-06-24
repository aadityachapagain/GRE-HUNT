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
             --usage <write the use of word in manykind>

EOF
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
                         if [ $# -gt 0 ]; then
                            if [ "$1" == "--speech" ]; then
                                shift
                                speech="${1// /_}"
                                shift
                            else
                                speech=""
                            fi
                        fi
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
                            python app.py --append $arg1 ---speech $speech --meaning $arg2
                         fi
                         ;;

        list )           shift
                         python app.py --list $1
                         ;;

        list-all )       shift
                         python app.py --list-all $1
                         ;;

        --help | -h )    usage
                         ;;
        * )              wrong_command
                         
    esac
else
    usage
fi