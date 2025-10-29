#!/bin/python3

import sys
import os
import platform
import re
from sorter import Sorter

class Engine:
    def __init__(self, verbose = False, debug = False):
        self.verbose : bool = debug if debug else verbose
        self.debug : bool = debug
        if self.verbose:
            print(f"Verbose is set on: {verbose}")
        if self.debug:
            print(f"Debug is set on: {debug}")

        self.path_sep : str = "\\" if platform.system() == "Windows" else "/"
        if self.debug:
            print(f"Detected system is: {platform.system()}. Path separator set on {self.path_sep}")
        
        self.root_dir : str = f"{os.getcwd()}{self.path_sep}"
        self.src_folder : str = None
        self.dst_folder : str = None

    def help(self):
        print(f"Usage is: {sys.argv[0]} [source-folder] [destination-folder]")
        print(f"    - source-folder: the folder from which the script takes files.")
        print(f"    - destination-folder: the folder where you will find ordered files.")
        print("")

    def check_paths(self):
        if not os.path.exists(self.src_folder):
            raise FileNotFoundError(f"The folder '{self.src_folder}' does not exist.")
        
        if not os.path.exists(self.dst_folder):
            os.makedirs(self.dst_folder)
        elif os.listdir(self.dst_folder):
            raise FileExistsError(f"Folder '{self.dst_folder}' already exists in current location.")

    def compose_paths(self):
        if platform.system() == "Windows":
            self.src_folder = sys.argv[1] if re.search(f"[A-Z]:{self.path_sep}", sys.argv[1]) else self.root_dir + sys.argv[1]
            self.dst_folder = sys.argv[2] if re.search(f"[A-Z]:{self.path_sep}", sys.argv[2]) else self.root_dir + sys.argv[2]
            if not self.src_folder.endswith(self.path_sep):
                self.src_folder += self.path_sep
            if not self.dst_folder.endswith(self.path_sep):
                self.dst_folder += self.path_sep
        else:
            self.src_folder = sys.argv[1] if sys.argv[1].startswith(self.path_sep) else self.root_dir + sys.argv[1]
            self.dst_folder = sys.argv[2] if sys.argv[2].startswith(self.path_sep) else self.root_dir + sys.argv[2]
            if not self.src_folder.endswith(self.path_sep):
                self.src_folder += self.path_sep
            if not self.dst_folder.endswith(self.path_sep):
                self.dst_folder += self.path_sep

        if self.verbose:
            print(f"Source folder path is: {self.src_folder}")
            print(f"Destination folder path is: {self.dst_folder}")

    def sort_files(self):
        print(f"Current working directory is: {self.root_dir}")
        
        Sorter(self.root_dir, self.src_folder, self.dst_folder, verbose=self.verbose, debug=self.debug).divide_by_year()