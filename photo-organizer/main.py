#!/bin/python3

from engine import Engine
import sys

### VERBOSITY ###
verbose = False
debug = False

if "--verbose" in sys.argv:
    verbose = True
    sys.argv.remove("--verbose")
if "--debug" in sys.argv:
    debug = True
    sys.argv.remove("--debug")

print(f"Verbose is set on: {verbose}")
print(f"Debug is set on: {debug}")

### FUNCTIONALITY ###
app = Engine(verbose=verbose, debug=debug)

# HELP
if "--help" in sys.argv:
    app.help()
    sys.argv.remove("--help")

# SORTING
if len(sys.argv) == 3:
    app.src_folder = sys.argv[1]
    app.dst_folder = sys.argv[2]

    print(f"Current working directory is: {app.root_dir}")
    app.compose_paths()
    app.check_paths()
    app.sort_files()