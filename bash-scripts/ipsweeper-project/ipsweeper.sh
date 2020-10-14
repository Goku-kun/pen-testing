
#! /bin/bash

# Enter the first three parts of IP address as the command line argument 1
if [ "$1" == "" ]
then
echo "You forgot to enter an IP address"
echo "Syntax: ./ipsweeper.sh 192.168.0"

else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":"&
done
fi
