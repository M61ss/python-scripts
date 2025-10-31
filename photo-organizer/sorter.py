#!/bin/python3

import os
import shutil
import analyzer

def divide_by_year(SRC_FOLDER : str, DST_FOLDER : str, PATH_SEP : str, verbose : bool = False, debug : bool = False):
    filenames, file_paths = analyzer.find_files(SRC_FOLDER, PATH_SEP)
    total_file_number = len(file_paths)
    file_dates = []

    for i, filename in enumerate(filenames):
        file_dates.append(analyzer.get_creation_date(filename))
        if verbose:
            print(f"{filename} creation date: {file_dates[i]}")
        if file_dates[i] in analyzer.YEARS:
            DST_SUBFOLDER = DST_FOLDER + file_dates[i]
            if not os.path.exists(DST_SUBFOLDER):
                os.makedirs(DST_SUBFOLDER)
            try:
                shutil.copy2(file_paths[i], DST_SUBFOLDER)
            except IOError:
                raise RuntimeError(f"Unable to copy from {file_paths[i]} to {DST_SUBFOLDER}")
            
    if len(file_dates) != total_file_number or len(file_paths) != total_file_number:
        raise RuntimeError("Filename list and file date length doesn't match.")
