# import pathlib
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
import hashlib

def add_mod_details(modconfigdata):
    print("Add author, version, description, date here.")
    modconfigdata['Author'] = input("Type the author of this modpack:\n")
    modconfigdata['Version'] = input("Type the version of this modpack:\n")
    modconfigdata['Description'] = input("Type a description of this modpack:\n")
    modconfigdata['Date'] = time.asctime()
    print("Date recorded as: " + modconfigdata['Date'])

    pass

def create_status_file(modpackPath):
    # we want to track what files are stored in a modpack, so we create a file recording all the related files.
    modconfigdata = read_all_added_files(modpackPath, os.listdir(modpackPath))
    # This JSON keeps track of whatever folder it's in and the files related to it.

    # Create a JSON with the changed files
    modconfig = os.path.join(modpackPath, "modtrackinginfo.json")
    with open(modconfig, 'w') as f:
        json.dump(modconfigdata, f, indent=4)
    print("modtrackinginfo.json generated.\n")
    create_hashlist(modpackPath, modconfigdata)
    time.sleep(1)
    pass

def read_all_added_files(modpackRoot, folderList):
    # check all files added into modpack folder and return a list
    # changedFiles = []
    # match folder name to keys in dictionary, then append file list
    changedFiles = {}

    # Allow user to enter author, description, etc. into dictionary
    add_mod_details(changedFiles)
    print("Changed files listed below:")
    for folders in range(len(os.listdir(modpackRoot))):
        currentFolder = os.path.join(modpackRoot, folderList[folders])
        if not os.path.isdir(currentFolder):
            continue
        changedFiles[folderList[folders]] = os.listdir(currentFolder)
        print(changedFiles[folderList[folders]])
        # print(folderList[folders] + " " + str(os.listdir(modpackRoot + "\\" + folderList[folders])))
    return changedFiles

def create_modpack(configdata):
    # handles the directory creation
    # if the directory is empty, prompt user to create a modpack folder or exit
    # emptyDirCheck = len(os.listdir(configdata['ProgramFolders']['modsDir'])) == 0
    # createNewMod = input("Mods directory is empty. Generate a new modpack? ") if emptyDirCheck else input("Existing modpacks found. Generate a new modpack? ")
    #
    # if createNewMod.lower() == "y":
    modName = generate_modpack_folders(configdata)
    if not modName:
        pass
    else:
        print("Modpack directory generated: " + modName)
        print("Add files to the folders, then use the \"Compile Modpack\" option.")
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

def create_hashlist(modpackPath, modconfigdata):
    modHashDict = {}
    for file in range(len(os.listdir(os.path.join(modpackPath, "files")))):
        with open(os.path.join(modpackPath, "files", modconfigdata['files'][file]),'rb', buffering=0) as f:
            modHashDict[modconfigdata['files'][file]] = hashlib.file_digest(f, 'sha256').hexdigest()
            # print(hashlib.file_digest(f, 'sha256').hexdigest())
    print(modHashDict)
    print("Files added/changed: " + str(len(modHashDict)))

    modhashfile = os.path.join(modpackPath, "hashlist.json")
    with open(modhashfile, 'w') as f:
        json.dump(modHashDict, f, indent=4)
    print("hashlist.json generated.\n")


    pass

def compile_modpack(configdata):
    # search for existing modpacks
    # read all files
    # create status file
    # allow additional data entry
    # prep for usage and swap
    print("Checking for existing modpacks...\n")
    emptyDirCheck = len(os.listdir(configdata['ProgramFolders']['modsDir'])) == 0
    print("No modpacks found. Try to create a modpack with the \"Create Modpack\" command, then try again.\n") if emptyDirCheck else print(
        "Existing modpacks found.\n")

    print("Choose the file path to your mod specific folder.\n")
    tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    modpackPath = filedialog.askdirectory()
    if modpackPath:
        create_status_file(Path(modpackPath))
    else:
        print("Action cancelled.")
    pass
