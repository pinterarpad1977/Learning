#!/bin/bash

#echo "You entered the argument: $1, $2, $3, $4"

# you need to run the script with an argument and that becomes $1, $2, $3 etc

# ---------------------------------

#lines=$(ls -lh $1 | wc -l)

#echo "The $1 directory contains $(($lines-1)) objects"
# the issue is that the argument is not mandatory

#-----------------------------------

lines=$(ls -lh $1 | wc -l)

if [ $# -ne 1 ]
then
    echo "This script requires exactly one directory path passed to it"
    echo "Please try again."
    exit 1
fi

echo "The $1 directory contains $(($lines-1)) objects"


