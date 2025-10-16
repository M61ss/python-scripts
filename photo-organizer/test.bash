#!/bin/bash
read -p "** Option --help will be tested **"
printf "\n"
./photo-organizer/main.py --help
read -p "** Script working will be tested (no verbosity) **"
printf "\n"
./photo-organizer/main.py galleria-A52 sorted/
read -p "Verbosity will be tested."
printf "\n"
rm -rf sorted
./photo-organizer/main.py galleria-A52 sorted/ --verbose
read -p "** Stop conditions will be tested **"
printf "\n"
read -p "** Next should stop since --help cause termination **"
printf "\n"
./photo-organizer/main.py --help galleria-A52 sorted/
read -p "** Next should stop since sorted already exists and it isn't empty **"
printf "\n"
./photo-organizer/main.py galleria-A52 sorted/
rm -rf sorted