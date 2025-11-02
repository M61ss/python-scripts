#!/bin/python3

from datetime import date
import os

YEARS : list[str] = [str(year) for year in range(2000, date.today().year + 1)]

def get_creation_date(filename : str):
    prefix : str = "IMG-" if filename.startswith("IMG-") else ""
    prefix = "VID-" if filename.startswith("VID-") else prefix
    for year in YEARS:
        if filename.startswith(f"{prefix}{year}"):
            return year
    return f"UNK"

def get_creation_dates(filenames : list[str]):
    file_dates = []
    for filename in filenames:
        file_dates.append(get_creation_date(filename))
    return file_dates

def find_files(SRC_FOLDER, PATH_SEP, verbose : bool = False, debug : bool = False):
    filenames : list[str] = []
    file_paths : list[str] = []
    for file_node in os.listdir(SRC_FOLDER):
        file_node_path : str = f"{SRC_FOLDER}{PATH_SEP}{file_node}"
        if os.path.isfile(file_node_path):
            if debug:
                print(f"Found file '{file_node}' at {file_node_path}")
            file_paths.append(file_node_path)
            filenames.append(file_node)

    if verbose:
        print(f"File name list:\n{filenames}")
        print("")
    print(f"Total number of file: {len(file_paths)}")
    print("")

    return filenames, file_paths