#!/bin/python3

from datetime import date
import platform
import os

YEARS : list[int] = [str(year) for year in range(2000, date.today().year + 1)]

def get_creation_date(filename):
    for year in YEARS:
        if year in filename:
            return year
    if platform.system() == "Windows":
        creation = os.path.getctime()
        print(f"Creation date for {filename}: {creation}")
        return creation
    return f"UNK"