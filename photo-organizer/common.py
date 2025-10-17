#!/bin/python3

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

def terminate(code, msg = None):
    if code == 0:
        print("")
        print(f"{bcolors.OKGREEN}{bcolors.BOLD}SUCCESS{bcolors.ENDC}")
        print("")
    else:
        print("")
        print(f"{bcolors.FAIL}{bcolors.BOLD}ERROR{bcolors.ENDC}")
        print("")
        print(f"CODE: {bcolors.BOLD}{code}{bcolors.ENDC}")
        print(f"MSG: {bcolors.BOLD}{msg}{bcolors.ENDC}")
        print("")
        exit(code)