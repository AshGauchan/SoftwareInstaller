# 1: Import modules
import requests, urllib, os, subprocess, sys
from urllib.request import urlretrieve
from pathlib import Path

# 2: Set varibales
url = ("https://central.github.com/deployments/desktop/desktop/latest/win32") # tuple i.e. immutable

file_path1 = "C:\\Users\\ashim\\Downloads"
file_path2 = str(Path.home() / "Downloads") # Save exe. to Downloads folder

a = str(Path.home())

print(file_path1)
print(file_path2)
print(a)


# file_path_alt = os.path.expanduser("~")+"C:\Users\ashim\Downloads"

file_name = "GitHubDesktopSetup-x64.exe"# File Name gotten from above link

file_a = file_path1+file_name
print(file_a)