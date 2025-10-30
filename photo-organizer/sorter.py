#!/bin/python3

import os
import platform
import shutil
import analyzer

class Sorter:
    def __init__(self, ROOT_DIR : str, SRC_FOLDER : str, DST_FOLDER : str, verbose : bool = False, debug : bool = False):
        self.verbose : bool = debug if debug else verbose
        self.debug : bool = debug

        self.PATH_SEP : str = "\\" if platform.system() == "Windows" else "/"
        self.ROOT_DIR : str = ROOT_DIR
        self.SRC_FOLDER : str = SRC_FOLDER
        self.DST_FOLDER : str = DST_FOLDER
        self.filenames : list[str] = []
        self.file_paths : list[str] = []
        self.file_dates : list[str] = []
        self.total_file_number : int = 0

    def divide_by_year(self):
        self.filenames, self.file_paths = analyzer.find_files(self.SRC_FOLDER, self.PATH_SEP)
        self.total_file_number = len(self.file_paths)

        for i, filename in enumerate(self.filenames):
            self.file_dates.append(analyzer.get_creation_date(filename))
            if self.verbose:
                print(f"{filename} creation date: {self.file_dates[i]}")
            if self.file_dates[i] in analyzer.YEARS:
                DST_SUBFOLDER = self.DST_FOLDER + self.file_dates[i]
                if not os.path.exists(DST_SUBFOLDER):
                    os.makedirs(DST_SUBFOLDER)
                try:
                    shutil.copy2(self.file_paths[i], DST_SUBFOLDER)
                except IOError:
                    raise RuntimeError(f"Unable to copy from {self.file_paths[i]} to {DST_SUBFOLDER}")

        if len(self.file_dates) != self.total_file_number or len(self.file_paths) != self.total_file_number:
            raise RuntimeError("Filename list and file date length doesn't match.")
            
