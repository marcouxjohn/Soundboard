# FILE:     fileFunctions.py
# AUTHOR:   David LeBlanc 143807L@acadiau.ca
# DATE:     2019/11/17
# VERSION:  1.0
# PURPOSE:  This program defines functions for use in managing the files needed
# for the Chadatonic.

# Test

import sys
import tkinter as tk
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
def import_sound(soundPath):
    ext = str(os.path.splitext(soundPath)[1])
    path = str(Path(soundPath).stem)
    copyfile(soundPath, "sounds/" + path + ext)