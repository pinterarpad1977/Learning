#!/bin/bash

# update script which runs on multiple distros

if [ -d /etc/pacman.d ]
then
    # The host is based on Arch Linux, run the pacman update command
   sudo pacman -Syu
fi

if [ -d /etc/apt ]
then
    # the host is Debian or Ubuntu, run apt
    sudo apt update
    sudo apt dist-upgrade
fi

# --------------------------------------------------

# improved solution 1

release_file=/etc/os-release

if grep -q "Arch" $release_file # -q means quiet mode -> no output
then
    # The host is based on Arch Linux, run the pacman update command
   sudo pacman -Syu
fi

if grep -q "Ubuntu" $release_file || grep -q "Debian" $release_file || grep -q "Mint" $release_file
then
    # the host is Ubuntu or Debian, run apt
    sudo apt update
    sudo apt dist-upgrade
fi
