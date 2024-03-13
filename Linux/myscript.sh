#!/bin/bash

#echo "Hello World!"
#echo "My current directory is:"
#pwd
myname="RP"
myage="47"
#echo "Hello, my name is $myname."
#with single quotes it will print $myname instead of the variable value 
#echo 'Hello, my name is $myname.'
#echo "I'm $myage years old."

#save the output of a command to a variable:
now=$(date)
#echo "Hello $myname"
#echo "The system time and date is:"
#echo $now
#echo "Your username is: $USER"

# MATH do not use spaces at assignment of numbers!
num1=100
num2=3
#echo $(( num1 + num2 ))

# IF - pay attention to spaces!

#if [ $num1 -eq 100 ]
#then
#    echo "The condition is true."
#else
#    echo "The condition is false."
#fi

# comparison:
# -eq : equals
# -ne : not equals
# -gt : greater than
# -f  : checks if a file exists
# !   : reverses the logic

if [ -f ~/myfile ]
then
    echo "The file already exists."
else
    echo "The file doesn't exist."
fi



