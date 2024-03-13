#!/bin/bash

# the $? variable stores the exit code of the previous command
# 0 = success, not 0 means error

package=htop

#sudo apt install $package

#echo "The exit code for $package install was: $?"

#if [ $? -eq 0 ]
#then
#    echo "The installation of $package was successful"
#    echo "The new command is here"
#    which $package
#else
#    echo "$package failed to install."
#fi


sudo apt install $package >> package_install.log

#echo "The exit code for $package install was: $?"

if [ $? -eq 0 ]
then
    echo "The installation of $package was successful"
    echo "The new command is here"
    which $package

else
    echo "$package failed to install." >> failure.log
fi
