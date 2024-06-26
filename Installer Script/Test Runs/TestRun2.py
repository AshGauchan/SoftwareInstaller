"""
- Script to Automate installation of applications/software to Windows directory
    - via running this script as an executable in the terminal

RUN2: 
    - Code that executes the download via Python PIP (i.e. as automated/efficent as you can get)
"""

# 1: Import required module + Declare 
import os, subprocess

# 1.5: Set variables to keep clean
global url_link, inst_path 

#url_link = "https://central.github.com/deployments/desktop/desktop/latest/win32"
install_path = "C:\Program Files"
app = "github"

# 2: Function to install Software

def install_package(pkg):
    subprocess.call(["pip", "install", pkg])
    print(f"{pkg} is now installed!")

