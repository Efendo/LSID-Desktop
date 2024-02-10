# Import necessary modules
from whiptail import Whiptail  
import os
import subprocess
import getpass

# Get current username
user = getpass.getuser()  

# Create main Whiptail window 
window = Whiptail(title="LSID Desktop", backtitle=f"USER: {user}, OS based on: {os.name}")

# Show welcome message box
window.msgbox("Welcome to LSID Desktop")   

# Define menu function to show menu and get selection
def menu():
    window = Whiptail(title="LSID Desktop: Menu", backtitle=f"USER: {user}, OS based on: {os.name}")
    me=window.menu("What do you want to do today?", ["Do Math", "Play a Game", "End LSID Desktop"])[0]
    return me

# Main loop
while True:
    # Show menu and get selection
    me = menu()
    
    # Check if "End LSID Desktop" was not selected
    if me != "End LSID Desktop":
        # Show message box with selection
        window.msgbox(me)  
        
    else:
        # Show ending message
        window.msgbox("Ending LSID Desktop...")
    
    # Check if end was selected    
    if me == "End LSID Desktop":
        # Exit program
        exit()
