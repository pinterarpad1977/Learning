#!/bin/bash

#command=usr/bin/htop

# if we use [ ] in an is the we are actually using the test command

#if [ -f $command ]
#then
#    echo "$command is available, running it..."
#else
#    echo "$command is NOT available, installing it..."
#    sudo apt update && sudo apt install -y htop
#fi

#$command

# && chains commands together (if the first command is successful runs the second one too
# -y assume yes (don't ask questions)

#better version:
command=htop

if command -v $command
then
    echo "$command is available, running it..."
else
    echo "$command is NOT available, installing it..."
    sudo apt update && sudo apt install -y $command
fi

$command

# command -v is a command which checks if a command exists or not
