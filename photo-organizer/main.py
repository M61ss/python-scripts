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

app = Engine(verbose=verbose, debug=debug)

# HELP
if "--help" in sys.argv:
    app.help()
    exit(0)

# SORTING
if len(sys.argv) == 3:
    try:
        app.compose_paths(sys.argv[1], sys.argv[2])
        app.sort_files()
    except BaseException as e:
        print(e)
else:
    app.help()
    raise RuntimeError("Too few arguments.")