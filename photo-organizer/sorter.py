#!/bin/python3
import os
import re
import shutil
from datetime import date
from common import terminate, bcolors

class Sorter:
    def __init__(self, ROOT_DIR, SOURCE_FOLDER_PATH, DESTINATION_FOLDER_PATH, verbose):
        self.verbose = verbose
        self.ROOT_DIR = ROOT_DIR
        self.SOURCE_FOLDER_PATH = SOURCE_FOLDER_PATH
        self.DESTINATION_FOLDER_PATH = DESTINATION_FOLDER_PATH
        self.years = [str(year) for year in range(2000, date.today().year + 1)]
        self.filenames = []
        self.file_paths = []
        self.file_dates = []
        self.total_file_number = 0

    def get_taken_date(self, filename):
        for year in self.years:
            if year in filename:
                return year
        return f"{bcolors.WARNING}NO-TAKEN-DATE{bcolors.ENDC}"
    
    def inspector(self):
        for file_node in os.listdir(self.SOURCE_FOLDER_PATH):
            file_node_path = f"{self.SOURCE_FOLDER_PATH}/{file_node}"
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
            terminate(0)

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
                    terminate(4, f"Unable to copy from {self.file_paths[i]} to {DESTINATION_SUBFOLDER_PATH}")

        if len(self.file_dates) != self.total_file_number or len(self.file_paths) != self.total_file_number:
            terminate(3, "Filename list and file date list have different size.")
            
