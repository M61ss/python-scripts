#!/bin/python3

import os
import platform
import re
import shutil
from datetime import date
from common import bcolors

class Sorter:
    def __init__(self, ROOT_DIR : str, SOURCE_FOLDER_PATH : str, DESTINATION_FOLDER_PATH : str, verbose : bool = False, debug : bool = False):
        self.verbose : bool = verbose
        self.debug : bool = debug

        self.path_sep : str = "\\" if platform.system() == "Windows" else "/"
        self.ROOT_DIR : str = ROOT_DIR
        self.SOURCE_FOLDER_PATH : str = SOURCE_FOLDER_PATH
        self.DESTINATION_FOLDER_PATH : str = DESTINATION_FOLDER_PATH
        self.years : list[int] = [str(year) for year in range(2000, date.today().year + 1)]
        self.filenames : list[str] = []
        self.file_paths : list[str] = []
        self.file_dates : list[str] = []
        self.total_file_number : int = 0

    def get_taken_date(self, filename):
        for year in self.years:
            if year in filename:
                return year
        return f"{bcolors.WARNING}NO-TAKEN-DATE{bcolors.ENDC}"
    
    def inspector(self):
        for file_node in os.listdir(self.SOURCE_FOLDER_PATH):
            file_node_path : str = f"{self.SOURCE_FOLDER_PATH}{self.path_sep}{file_node}"
            if os.path.isfile(file_node_path):
                if self.verbose:
                    print(f"Found file '{file_node}' at {file_node_path}")
                self.file_paths.append(file_node_path)
                self.filenames.append(file_node)
        self.total_file_number = len(self.file_paths)

        if self.verbose:
            print(f"File name list:\n{self.filenames}")
            print("")
        print(f"Total number of file: {bcolors.BOLD}{self.total_file_number}{bcolors.ENDC}")
        print("")
        if not re.search("y|| ", input("Is it ok to proceed ([y]/n)? ")):
            return 0, None

    def sort(self):
        self.inspector()

        for i, filename in enumerate(self.filenames):
            self.file_dates.append(self.get_taken_date(filename))
            if self.verbose:
                print(f"{filename} creation date: {self.file_dates[i]}")
            if self.file_dates[i] in self.years:
                DESTINATION_SUBFOLDER_PATH = self.DESTINATION_FOLDER_PATH + self.file_dates[i]
                if not os.path.exists(DESTINATION_SUBFOLDER_PATH):
                    os.makedirs(DESTINATION_SUBFOLDER_PATH)
                try:
                    shutil.copy2(self.file_paths[i], DESTINATION_SUBFOLDER_PATH)
                except IOError:
                    return {4 : f"Unable to copy from {self.file_paths[i]} to {DESTINATION_SUBFOLDER_PATH}"}

        if len(self.file_dates) != self.total_file_number or len(self.file_paths) != self.total_file_number:
            return 3, "Filename list and file date list have different size."
            
