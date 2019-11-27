# FILE:     fileFunctions.py
# AUTHOR:   David LeBlanc 143807L@acadiau.ca
# DATE:     2019/11/22
# VERSION:  1.2
# PURPOSE:  This program defines functions for use in managing the files needed
# for the Chadatonic.

import sys
import tkinter as tk
import json
from tkinter import filedialog
import os
from shutil import copyfile
from pathlib import Path

# Opens a file selection prompt and returns the selected path
def file_prompt():
    root = tk.Tk()
    root.withdraw()
    filePath = filedialog.askopenfilename()

    return filePath

# Creates the directories for configurations and sounds, if they don't already
# exist
def create_directories():
    if not os.path.exists("configs"):
        os.mkdir("configs")
    if not os.path.exists("sounds"):
        os.mkdir("sounds")


# Imports a selected sound into the sounds folder so it is easy to find
# Returns -1 on error, 0 on success
def import_sound(soundPath):
    ext = str(os.path.splitext(soundPath)[1])
    path = str(Path(soundPath).stem)

    # Return error if unusable format
    if ext != ".wav":
        return -1

    # Return error if directories do not exist
    if not os.path.exists("sounds"):
        return -1

    copyfile(soundPath, "sounds/" + path + ext)

    return 0

# Saves a sound config with given settings in configData for given configName
# configData[0]:    Sound name
# configData[1]:    Volume
# configData[2]:    Amplitude
# configData[3]:    Whether to loop (True) or not (False)
# configData[4]:    How many times to loop, if enabled
# configData[5]:    Whether or not the filter is enabled
# configData[6]:    
# configName:       The name of the config in use (folder)
def save_sound_config(configData, configName):
    # If config folder does not exist, error
    if not os.path.exists("configs"):
        return -1

    # Determine config path
    configFolder = "configs/" + configName
    configPath = configFolder + "/" + configData[0] + ".json"

    # Create config content
    data = {}
    data["content"] = []
    data["content"].append({
        "soundname":    configData[0],
        "volume":       configData[1],
        "amplitude":    configData[2],
        "loopOn":       configData[3],
        "loopCount":    configData[4],
        "filter":       configData[5]
    })

    # Create config if it doesn't exist
    if not os.path.exists(configFolder):
        os.mkdir(configFolder)

    with open(configPath, 'w') as outfile:
        json.dump(data, outfile)

    return 1

# Returns the config data for a specified sound, or -1 on failure
# returnData[0]: sound name
# returnData[1]: volume
# returnData[2]: amplitude
# returnData[3]: Whether to loop (true) or not (false)
# returnData[4]: How many times to loop, if enabled
# returnData[5]: Whether or not the filter is enabled
# returnData[6]: config key
def load_sound_config(soundName, configName):
    returnData = [None]*2

    # Determine  config path
    configPath = "configs/" + configName + "/" + soundName + ".json"

    if not os.path.exists(configPath):
        return -1

    # Open JSON
    with open("configs/" + soundName + ".json") as config_file:
        data = json.load(config_file)
        # Loop through file to find the correct sound
        for sound in data['content']:
            if sound["soundname"] == soundName:
                returnData[0] = sound["soundname"]
                returnData[1] = sound["volume"]
                returnData[2] = sound["amplitude"]
                returnData[3] = sound["loopOn"]
                returnData[4] = sound["loopCount"]
                returnData[5] = sound["Filter"]

    return returnData