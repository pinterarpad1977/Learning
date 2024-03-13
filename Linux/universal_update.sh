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

# ------- improved solution 1 ------------------------

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

# -------- improved solution 2 ---------------------

release_file=/etc/os-release
logfile=/var/log/updater.log
errorlog=/var/log/updater_error.log

if grep -q "Arch" $release_file # -q means quiet mode -> no output
then
    # The host is based on Arch Linux, run the pacman update command
    sudo pacman -Syu 1>>$logfile 2>>$errorlog
    if [ $? -ne 0 ]
    then
	echo "An error occured, please check the $errorlog file."
    fi
fi

if grep -q "Ubuntu" $release_file || grep -q "Debian" $release_file || grep -q "Mint" $release_file
then
    # the host is Ubuntu or Debian, Linux Mint run apt
    sudo apt update 1>>$logfile 2>>$errorlog
    if [ $? -ne 0 ]
    then
	echo "An error occured, please check the $errorlog file."
    fi
    sudo apt dist-upgrade 1>>$logfile 2>>$errorlog
    if [ $? -ne 0 ]
    then
	echo "An error occured, please check the $errorlog file."
    fi
fi


# -------- improved solution 3 ---------------------
# introducing functions

check_exit_status() {
    if [ $? -ne 0 ]
    then
	echo "An error occured, please check the $errorlog file."
    fi
}

release_file=/etc/os-release
logfile=/var/log/updater.log
errorlog=/var/log/updater_error.log

if grep -q "Arch" $release_file # -q means quiet mode -> no output
then
    # The host is based on Arch Linux, run the pacman update command
    sudo pacman -Syu 1>>$logfile 2>>$errorlog
    check_exit_status
fi

if grep -q "Ubuntu" $release_file || grep -q "Debian" $release_file || grep -q "Mint" $release_file
then
    # the host is Ubuntu or Debian, Linux Mint run apt
    sudo apt update 1>>$logfile 2>>$errorlog
    check_exit_status

    sudo apt dist-upgrade -y 1>>$logfile 2>>$errorlog
    check_exit_status
fi


# -------- improved solution 4 ---------------------
# introducing case

check_exit_status() {
    if [ $? -ne 0 ]
    then
	echo "An error occured, please check the $errorlog file."
    fi
}

release_file=/etc/os-release
logfile=/var/log/updater.log
errorlog=/var/log/updater_error.log

if grep -q "Arch" $release_file # -q means quiet mode -> no output
then
    # The host is based on Arch Linux, run the pacman update command
    sudo pacman -Syu 1>>$logfile 2>>$errorlog
    check_exit_status
fi

if grep -q "Ubuntu" $release_file || grep -q "Debian" $release_file || grep -q "Mint" $release_file
then
    # the host is Ubuntu or Debian, Linux Mint run apt
    sudo apt update 1>>$logfile 2>>$errorlog
    check_exit_status

    sudo apt dist-upgrade -y 1>>$logfile 2>>$errorlog
    check_exit_status
fi

