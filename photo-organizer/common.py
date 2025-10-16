#!/bin/python3
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def help():
    print(f"Usage is: {sys.argv[0]} [source-folder] [destination-folder]")
    print(f"    - {bcolors.BOLD}source-folder{bcolors.ENDC}: the folder from which the script takes files.")
    print(f"    - {bcolors.BOLD}destination-folder{bcolors.ENDC}: the folder where you will find ordered files.")

def terminate(code, msg = None):
    if code == 0:
        print(f"{bcolors.OKGREEN}{bcolors.BOLD}\nSUCCESS\n{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}{bcolors.BOLD}\nERROR: {msg}\n{bcolors.ENDC}")
    exit(code)