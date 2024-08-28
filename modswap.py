import sys
import os
import json
import time
from pathlib import Path
from atomicswap import swap

def swap_dialog():
    # ask user if they want to swap modpacks, or individual files.
    pass

def swap_handler(modfile, textfile):
    # if modpack, get all files
    # base_dir = os.path.normpath("C:\\Users\\smasi\\PycharmProjects\\RidersModManager\\Mods\\modfile.txt")
    # new_dir = os.path.normpath("C:\\Users\\smasi\\PycharmProjects\\RidersModManager\\Textures\\texturefile.txt")
    # swap(base_dir, new_dir)
    swap(modfile, textfile)
    # swap(base_dir)
    pass