#!/bin/bash

######################################### HELP

echo "*** HELP TEST START ***"
printf "\n"

./main.py --help

printf "\n"
echo "*** HELP TEST END ***"

######################################### FUNCTIONAL

echo "*** FUNCTIONAL TEST START ***"
printf "\n"

./main.py test-batch sorted/

printf "\n"
echo "*** FUNCTIONAL TEST END ***"

######################################### VERBOSITY

echo "*** VERBOSITY TEST START ***"
printf "\n"

echo "  1. Checking --verbose output"
printf "\n"
rm -rf sorted
./main.py test-batch sorted/ --verbose
printf "\n"

echo "  2. Checking --debug output"
printf "\n"
rm -rf sorted
./main.py test-batch sorted/ --verbose --debug

printf "\n"
echo "*** VERBOSITY TEST END ***"

######################################### STOP

echo "*** STOP CONDITION TEST START ***"
printf "\n"

echo "  1. Already existing not empty folder should cause termination"
printf "\n"
./main.py test-batch sorted/

printf "\n"
echo "*** STOP CONDITION TEST END ***"