#!/bin/python3
import sys
import os
import platform
import re
from common import terminate, help, bcolors
from sorter import Sorter

class App:
    def __init__(self, verbose = False):
        self.verbose = verbose
        self.ROOT_DIR = f"{os.getcwd()}\\" if platform.system() == "Windows" else f"{os.getcwd()}/"
        self.source_folder_path = None
        self.destination_folder_path = None

    def validate_params(self):
        if "--help" in sys.argv:
            help()
            terminate(0)
        if "--verbose" in sys.argv:
            self.verbose = True
            sys.argv.remove("--verbose")

    def check_paths(self):
        if not os.path.exists(self.source_folder_path):
            terminate(2, f"The folder '{self.source_folder_path}' does not exist.")
        if not os.path.exists(self.destination_folder_path):
            os.makedirs(self.destination_folder_path)
        elif os.listdir(self.destination_folder_path):
            terminate(2, f"Folder '{self.destination_folder_path}' already exists in current location.")
        print("")

    def compose_paths(self):
        if platform.system() == "Windows":
            self.source_folder_path = sys.argv[1] if re.search("?:\\", sys.argv[1]) else self.ROOT_DIR + sys.argv[1]
            self.destination_folder_path = sys.argv[2] if re.search("?:\\", sys.argv[2]) else self.ROOT_DIR + sys.argv[2]
            if not self.source_folder_path.endswith("\\"):
                self.source_folder_path += "\\"
            if not self.destination_folder_path.endswith("\\"):
                self.destination_folder_path += "\\"
        else:
            self.source_folder_path = sys.argv[1] if sys.argv[1].startswith("/") else self.ROOT_DIR + sys.argv[1]
            self.destination_folder_path = sys.argv[2] if sys.argv[2].startswith("/") else self.ROOT_DIR + sys.argv[2]
            if not self.source_folder_path.endswith("/"):
                self.source_folder_path += "/"
            if not self.destination_folder_path.endswith("/"):
                self.destination_folder_path += "/"
        print(f"Source folder path is: {self.source_folder_path}")
        print(f"Destination folder path is: {self.destination_folder_path}")

if __name__=="__main__":
    app = App()
    app.validate_params()
    print(f"Current working directory is: {bcolors.BOLD}{app.ROOT_DIR}{bcolors.ENDC}")
    app.compose_paths()
    app.check_paths()

    print(f"Verbose is set on: {bcolors.BOLD}{app.verbose}{bcolors.ENDC}")

    sorter = Sorter(app.ROOT_DIR, app.source_folder_path, app.destination_folder_path, app.verbose)
    sorter.sort()
    terminate(0)