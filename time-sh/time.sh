#!/bin/sh

Iterations=$1

if [[ $Iterations =~ ^-?[0-9]+$ ]] 
then
    for k in $(seq 1 $Iterations)
    do
        date +'%Y.%m.%d %H:%M:%S' && sleep 3    # Format YYYY.MM.DD HH:MM:SS
    done
    echo "Total iterations: $Iterations"
else echo "Error..."; exit 1
fi
