import sys
import os
import json
import time
from tkinter import *
from tkinter import ttk
from modswap import *
import requests
from pathlib import Path
import tkinter
from tkinter import filedialog

def create_status_file():
    # we want to track what files are stored in a modpack, so we create a file recording all the related files.
    read_all_added_files()
    # pass this list in and create a JSON with the changed files
    # configdata = {
    #     "ProgramFolders": {
    #         "modsDir": "",
    #         "texturesDir": ""
    #     },
    #     "GameFolders": {
    #         "discDir": "",
    #         "filesDir": "",
    #         "sysDir": "",
    #         "texturesDir": ""
    #     }
    # }
    # with open(configfile, 'w') as f:
    #     json.dump(configdata, f, indent=4)
    # print("Settings.json generated.\n")
    # time.sleep(1)
    pass

def read_all_added_files():
    # check all files added into modpack folder and return a list
    pass

def create_modpack(configdata):
    # handles the file packing and recording of what files are included
    # if the directory is empty, prompt user to create a modpack folder or exit
    if len(os.listdir(configdata['ProgramFolders']['modsDir'])) == 0 or input("Generate mods? ").lower() == "y":
        createNewMod = input("Mods directory is empty. Generate a new modpack? ")
        if createNewMod.lower() == "y":
            modName = generate_modpack_folders(configdata)
            if not modName:
                pass
            else:
                print("Modpack directory generated: " + modName)
            pass
        else:
            print("Skipped creating modpack.")
            return

    # print("Choose the file path to your mod specific folder.")
    # tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    # modpackPath = filedialog.askdirectory()
    pass

def generate_modpack_folders(configdata):
    # simply generate folder setup for the user
    newModpackName = input("Enter the name of your new modpack: ")
    newModpackName = configdata['ProgramFolders']['modsDir'] + "\\" + newModpackName
    try:
        os.mkdir(newModpackName)
        os.mkdir(newModpackName + '\\sys')
        os.mkdir(newModpackName + '\\files')
        os.mkdir(newModpackName + '\\textures')
    except:
        print("Directory already exists.")
        return ""

    return newModpackName