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

    def divide_by_year(self):
        filenames, file_paths = analyzer.find_files(self.SRC_FOLDER, self.PATH_SEP)
        total_file_number = len(file_paths)
        file_dates = []

        for i, filename in enumerate(filenames):
            file_dates.append(analyzer.get_creation_date(filename))
            if self.verbose:
                print(f"{filename} creation date: {file_dates[i]}")
            if file_dates[i] in analyzer.YEARS:
                DST_SUBFOLDER = self.DST_FOLDER + file_dates[i]
                if not os.path.exists(DST_SUBFOLDER):
                    os.makedirs(DST_SUBFOLDER)
                try:
                    shutil.copy2(file_paths[i], DST_SUBFOLDER)
                except IOError:
                    raise RuntimeError(f"Unable to copy from {file_paths[i]} to {DST_SUBFOLDER}")

        if len(file_dates) != total_file_number or len(file_paths) != total_file_number:
            raise RuntimeError("Filename list and file date length doesn't match.")
            
