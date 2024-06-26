"""
- Script to Automate installation of applications/software to Windows directory
    - via running this script as an executable in the terminal

RUN1: 
    - Code that executes the download via URL (i.e. how someone would do to manually)
"""

# 1: Import required module + Declare 
import os, subprocess, urllib.request as pull_req

# 1.5: Set variables to keep code clean
global url_link, app_executable, install_path 

url_link = "https://central.github.com/deployments/desktop/desktop/latest/win32"
app_executable = "github_installer.exe"
#install_path = "C:\Users\ashim\Documents\Python Scripts\SL DevOps Training\Weekly Tasks\07_06\Box"


# 2: Function to install GitHub 
def install_package(pkg):
    try:
        if pkg == "github":
            pull_req.urlretrieve(url_link, app_executable) # donwloads github 
            #subprocess.check_call([app_executable, "-ms"]) # installs silently
            #os.remove(app_executable) # removes package after download
            print(f"{pkg} installed sucessfully!")
    except subprocess.CalledProcessError:
        print(f"{pkg} failed to instal!?")


install_package(pkg="github")

# 3: Clean up files that were downloaded
        