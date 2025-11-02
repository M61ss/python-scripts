#!/bin/python3

import sys
import os
import platform
import re
import sorter

class Engine:
    def __init__(self, verbose = False, debug = False):
        self.verbose : bool = debug if debug else verbose
        self.debug : bool = debug
        if self.verbose:
            print(f"Verbose is set on: {verbose}")
        if self.debug:
            print(f"Debug is set on: {debug}")

        self.PATH_SEP : str = "\\" if platform.system() == "Windows" else "/"
        if self.debug:
            print(f"Detected system is: {platform.system()}. Path separator set on {self.PATH_SEP}")
        
        self.root_dir : str = f"{os.getcwd()}{self.PATH_SEP}"
        self.src_folder : str = None
        self.dst_folder : str = None

    def help(self):
        print(f"Usage is: {sys.argv[0]} [source-folder] [destination-folder]")
        print(f"    - source-folder: the folder from which the script takes files.")
        print(f"    - destination-folder: the folder where you will find ordered files.")

    def check_paths(self):
        if not os.path.exists(self.src_folder):
            raise FileNotFoundError(f"The folder '{self.src_folder}' does not exist.")
        
        if not os.path.exists(self.dst_folder):
            os.makedirs(self.dst_folder)
        elif len(os.listdir(self.dst_folder)) > 0:
            raise FileExistsError(f"Folder '{self.dst_folder}' already exists in current location.")

    def compose_paths(self, src_path : str, dst_path : str):
        if platform.system() == "Windows":
            self.src_folder = src_path if re.search(f"[A-Z]:{self.PATH_SEP}", src_path) else self.root_dir + src_path
            self.dst_folder = dst_path if re.search(f"[A-Z]:{self.PATH_SEP}", dst_path) else self.root_dir + dst_path
            if not self.src_folder.endswith(self.PATH_SEP):
                self.src_folder += self.PATH_SEP
            if not self.dst_folder.endswith(self.PATH_SEP):
                self.dst_folder += self.PATH_SEP
        else:
            self.src_folder = src_path if src_path.startswith(self.PATH_SEP) else self.root_dir + src_path
            self.dst_folder = dst_path if dst_path.startswith(self.PATH_SEP) else self.root_dir + dst_path
            if not self.src_folder.endswith(self.PATH_SEP):
                self.src_folder += self.PATH_SEP
            if not self.dst_folder.endswith(self.PATH_SEP):
                self.dst_folder += self.PATH_SEP

        self.check_paths()

        if self.verbose:
            print(f"Source folder path is: {self.src_folder}")
            print(f"Destination folder path is: {self.dst_folder}")

    def sort_files(self):
        print(f"Current working directory is: {self.root_dir}")
        sorter.divide_by_year(self.src_folder, self.dst_folder, self.PATH_SEP, self.verbose, self.debug)