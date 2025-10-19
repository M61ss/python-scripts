#!/bin/bash

echo "############## HELP "##############
printf "\n"

./main.py --help

echo "############## FUNCTIONAL "##############
printf "\n"

rm -rf sorted
./main.py test-batch sorted/

echo "############## VERBOSITY "##############
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

echo "############## STOP CONDITION TEST START "##############
printf "\n"

echo "  1. Already existing not empty folder should cause termination"
printf "\n"
./main.py test-batch sorted/