import sys
import os
import json
import time
from atomicswap import swap
from tkinter import *
from tkinter import ttk

import requests
from pathlib import Path
import tkinter
from tkinter import filedialog

def parse_settings(configfile):
    # if the file exists, start checking all parameters
    if os.path.isfile(configfile):
        print("Welcome to Riders Mod Manager: a universal tool to download, hotswap, add, create, and edit mod files for Sonic Riders.\n")
        time.sleep(1)
        # load json here
        configraw = open(configfile)
        configdata = json.load(configraw)
        # print(configdata)
        # check the working mods directory, working textures directory, and the working disc directory.
        # these are the most important parts involved, user must enter these or be set as default directories
        if not configdata['ProgramFolders']['modsDir']:
            print("Mods directory not defined. Please choose the folder where you store your working mod packs, or press cancel to use the default directory.")
            time.sleep(2)
            tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
            newModPath = filedialog.askdirectory()
            if newModPath:
                configdata['ProgramFolders']['modsDir'] = Path(newModPath)
            else:
                configdata['ProgramFolders']['modsDir'] = os.getcwd() + "\\Mods"
            print("New working mod files directory generated: " + configdata['ProgramFolders']['modsDir'] + "\n")
        else:
            # if it does exist, normpath just in case
            configdata['ProgramFolders']['modsDir'] = os.path.normpath(configdata['ProgramFolders']['modsDir'])
            print("Working mod files directory found in settings.json.")

        if not configdata['ProgramFolders']['texturesDir']:
            print("Textures directory not defined. Please choose the folder where you store your working textures directory, or press cancel to set the default directory.")
            time.sleep(2)
            tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
            newTexturePath = filedialog.askdirectory()
            if newTexturePath:
                configdata['ProgramFolders']['texturesDir'] = Path(newTexturePath)
            else:
                configdata['ProgramFolders']['texturesDir'] = os.getcwd() + "\\Textures"
            print("New working textures directory generated: " + configdata['ProgramFolders']['texturesDir'] + "\n")
        else:
            # if it does exist, normpath just in case
            configdata['ProgramFolders']['texturesDir'] = os.path.normpath(configdata['ProgramFolders']['texturesDir'])
            print("Working textures directory found in settings.json.")

        if not configdata['GameFolders']['discDir']:
            print("Extracted ISO directory not defined. Please choose the folder where you store your extracted ISO, or press cancel to set the default directory.")
            time.sleep(2)
            tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
            newDiscPath = filedialog.askdirectory()
            if newDiscPath:
                configdata['GameFolders']['discDir'] = Path(newDiscPath)
            else:
                configdata['GameFolders']['discDir'] = os.getcwd() + "\\ISOHere"
            print("New extracted ISO directory generated: " + configdata['GameFolders']['discDir'] + "\n")
        else:
            # if it does exist, normpath just in case
            configdata['GameFolders']['discDir'] = os.path.normpath(configdata['GameFolders']['discDir'])
            print("Extracted ISO directory found in settings.json.")
        with open(configfile, 'w') as f:
            json.dump(configdata, f, indent=4)


def generateSettings(configfile):
    # generate settings.json here
    configdata = {
        "ProgramFolders": {
            "modsDir": "",
            "texturesDir": ""
        },
        "GameFolders": {
            "discDir": "",
            "filesDir": "",
            "sysDir": "",
            "texturesDir": ""
        }
    }
    with open(configfile, 'w') as f:
        json.dump(configdata, f, indent=4)
    print("Settings.json generated.\n")
    time.sleep(1)
    pass

if __name__ == '__main__':
    path = os.getcwd()
    configpath = path + "\\settings.json"
    # Check if settings.json exists
    if not os.path.isfile(configpath):
        print("No settings.json found. Generating new file.")
        # Generate that here if it does not exist
        generateSettings(configpath)
    # parse file if it does
    parse_settings(configpath)
    # create the menu here and add options:

    # 1. Download modpacks from network - modserverwork.py
    # 2. Download files from network - modserverwork.py
    # 3. Compile modpack - modpacker.py
    # 4. Swap files - mod files/textures/modpacks - modswap.py
    # 5. Create ADX files for riders - ADXGen.py
    # 6. Send/receive mod files (requires two or more people with an internet connection) - modlinker.py
    # 7. Check/Verify stored modpacks and files - modcheck.py
    # 8. Exit

