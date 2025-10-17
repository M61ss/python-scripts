#!/bin/bash
read -p "*** HELP TEST ***"
printf "\n"
./test.py --help

read -p "*** FUNCTIONAL TEST ***"
printf "\n"
./test.py test-batch sorted/

read -p "*** VERBOSITY TEST ***"
printf "\n"
rm -rf sorted
./test.py test-batch sorted/ --verbose
rm -rf sorted
./test.py test-batch sorted/ --verbose --debug

read -p "*** STOP CONDITION TEST ***"
printf "\n"
read -p "1. Already existing not empty folder should cause termination"
printf "\n"
./test.py test-batch sorted/