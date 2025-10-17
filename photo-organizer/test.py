#!/bin/python3

from main import Engine
import sys
from common import bcolors

verbose = False
debug = False

if "--verbose" in sys.argv:
    verbose = True
    sys.argv.remove("--verbose")
if "--debug" in sys.argv:
    debug = True
    sys.argv.remove("--debug")

app = Engine(verbose=verbose, debug=debug)

if "--help" in sys.argv:
    app.help()
    sys.argv.remove("--help")

print(f"Current working directory is: {bcolors.BOLD}{app.ROOT_DIR}{bcolors.ENDC}")
app.compose_paths()
app.check_paths()

print(f"Verbose is set on: {bcolors.BOLD}{app.verbose}{bcolors.ENDC}")

sorter = Sorter(app.ROOT_DIR, app.source_folder_path, app.destination_folder_path, app.verbose)
sorter.sort()