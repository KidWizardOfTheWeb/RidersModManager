import sys
import os
import json
import time
from atomicswap import swap
from pathlib import Path
import tkinter
from tkinter import filedialog

def swap_dialog(configfile, modjson):
    # ask user if they want to swap modpacks, or individual files.
    if input("Test mod hotswap?").lower() == "y":
        swap_handler()
    else:
        return
    pass

def swap_handler(modfile, textfile):
    # if modpack, get all files
    # base_dir = os.path.normpath("C:\\Users\\smasi\\PycharmProjects\\RidersModManager\\Mods\\modfile.txt")
    # new_dir = os.path.normpath("C:\\Users\\smasi\\PycharmProjects\\RidersModManager\\Textures\\texturefile.txt")
    # swap(base_dir, new_dir)
    # swap(modfile, textfile)
    # swap(base_dir)
    print("Choose the file path to the mod you want to swap files between.\n")
    tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    modpackPath = filedialog.askdirectory()

    # now swap this with the extracted iso directory.
    # find file name matches, then swap.
    # continue until loop is finished.
    # generate file that says which files moved.
    # update json tracker in final destination to reflect what files were changed.
    # update json tracker in original place to reflect files that were moved in
    #
    pass