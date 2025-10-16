#!/bin/bash
read -p "*** HELP TEST ***"
printf "\n"
./main.py --help

read -p "*** FUNCTIONAL TEST ***"
printf "\n"
./main.py galleria-A52 sorted/

read -p "*** VERBOSITY TEST ***"
printf "\n"
rm -rf sorted
./main.py galleria-A52 sorted/ --verbose

read -p "*** STOP CONDITION TEST ***"
printf "\n"
read -p "    1. --help should cause termination"
printf "\n"
./main.py --help galleria-A52 sorted/
read -p "    2. Already existing not empty folder should cause termination"
printf "\n"
./main.py galleria-A52 sorted/
rm -rf sorted