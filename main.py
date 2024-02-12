# Import necessary modules
from whiptail import Whiptail  
import os
import getpass
from pathlib import Path
import sys
import subprocess

# Get current username
user = getpass.getuser()  

# Get home directory
home = str(Path.home())

# Create main Whiptail window 
window = Whiptail(title="LSID Desktop", backtitle=f"USER: {user}, OS based on: {os.name}")

# Show welcome message box
window.msgbox("Welcome to LSID Desktop")   

# Define menu function to show menu and get selection
def menu():
    window = Whiptail(title="LSID Desktop: Menu", backtitle=f"USER: {user}, OS based on: {os.name}")
    me=window.menu("What do you want to do today?", ["View a file", "End LSID Desktop"])[0]
    return me

def ViewFile():
    file=window.inputbox("Enter some text:", f"{home}/")[0]
    if os.path.isfile(file):
        with open(file) as f:
            window.msgbox(f.read())
    else:
        window.msgbox("That's a directory!")
        ViewFile()

# Main loop
while True:
    # Show menu and get selection
    me = menu()

    # DISPLAY FILE
    if me == "View a file":
        ViewFile()

    # Check if end was selected    
    if me == "End LSID Desktop":
        # Exit program
        exit()
