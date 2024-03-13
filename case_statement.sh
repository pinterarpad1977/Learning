#!/bin/bash

echo "What is your favorite distro?"

echo "1 - Arch"
echo "2 - CentOS"
echo "3 - Debian"
echo "4 - Mint"
echo "5 - Ubuntu"
echo "6 - Something else..."

read distro;

case $distro in
    1) "Arch is a rolling release.";;
    2) "CentOS is popular on servers.";;
    3) "Debian is a community distro.";;
    4) "Mint is popular on desktops.";;
    5) "Ubuntu is popular on both servers and desktops.";;
    6) "So many distributions eh?";;
    *) "invalid selection"
esac

