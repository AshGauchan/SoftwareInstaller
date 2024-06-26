"""
Trying to define the file path to download

"""
# 1: Import modules
import requests, urllib, os, subprocess, time, sys
from urllib.request import urlretrieve
from pathlib import path

# 2: Set varibales
url = ("https://central.github.com/deployments/desktop/desktop/latest/win32") # tuple i.e. immutable

file_path1 = "C:\\Users\\ashim\\Downloads\\" # Save exe. to Downloads folder

# file_path2 = str(Path.home() / "Downloads\\")
    # This gets the Home path if not known
# file_path = os.path.expanduser("~")+"C:\\Users\\ashim\\Downloads\\"

file_name = "GitHubDesktopSetup-x64.exe"# File Name gotten from above link

main_file = os.path.abspath(file_path1+file_name)
    #  abslt_path = os.path.abspath(abslt_path)

# 3: Download .exe GitHub & read the file
def download_file(url, main_file):
    with requests.get(url, stream=True) as r: 
        # GET request to pull in the URL HTTP response + streaming the response to capture metadata
        print(r.raise_for_status()) # Produce an error response from HTTP (if any)
        time.sleep(3)
        with open(main_file, "wb") as f: # Using File Handling ("wb") - Open's file and writes to binary
            for chunk in r.iter_content(chunk_size=8000): # Loop to read the meta data in 'chunks' to when Stream = True (in bytes)
                f.write(chunk) # Writes to file
            print(f"{file_name} downloaded sucessfully.")
            time.sleep(5)

# 4 Check if the file has write permissions
def check_write_permissions():
    try: 
        if os.access(main_file, os.W_OK):
            print(f"File {file_name} is writable.")
            time.sleep(5) # wait a few secs to read output
        else:
            print(f"File {file_name} is not writable!")
            time.sleep(5)
    except FileNotFoundError:
        print(f"Error {file_name} not found!?")
        time.sleep(5)
    except PermissionError:
        print(f"You dont have permissions to write on {file_name}!")
        time.sleep(5)


# 5: Run command to install file in Windows Powershell
def run_cmd(command):
    try:
        # Run powershell cmd
        subprocess.run(["powershell", "-command", command], check=True)
        print(f"{file_name} installed sucessfully.")
        time.sleep(5)
    except subprocess.CalledProcessError as e:
        print(f"{file_name} failed to install!")
        time.sleep(5)

# 6: Add Github to the Winodws Environment Variable path 
sys.path.append("C:\\Users\\ashim\\AppData\Local")
    # WHERE TO PUT?? -- in the Install Function OR Run Cmd Function


# Call Functions (RUNNNER)
download_file(url, main_file)

check_write_permissions()

#run_cmd(f"Start-Process -FilePath {main_file} -Verb RunAs -Wait") # Input Run command to Powershell