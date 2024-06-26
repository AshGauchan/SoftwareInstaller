
# 1: Import modules
import requests, urllib, os, subprocess, sys
from urllib.request import urlretrieve

# 2: Set varibales
url = ("https://central.github.com/deployments/desktop/desktop/latest/win32") # tuple i.e. immutable

file_path = "Downloads" # Save exe. to Downloads folder

file_name = f"{file_path}GitHubDesktopSetup-x64.exe"# File Name gotten from above link

"""
# 3: Check meta data of the URL
path, headers = urlretrieve(url, file_name)
    # urlretrieve returns 2 values i.e. path, headers
for name, value in headers.items():
    print(name, value)
"""
    
"""
Output of above code provides key data needed:
    - File saved to: GitHubDesktopSetup-x64.exe
    - Content-Length: 159078872 (~159 MB)
    - Content-Type: application/octet-stream (i.e. Binary File)
"""

# 4: Download .exe GitHub & read the file
def download_file(url, file_name):
    with requests.get(url, stream=True) as r: 
        # GET request to pull in the URL HTTP response + streaming the response to capture metadata
        r.raise_for_status() # Produce an error response from HTTP (if any)
        with open(file_name, "wb") as f:
            # Using File Handling ("wb") - Open's file and writes to binary
            for chunk in r.iter_content(chunk_size=8000):
                # Loop to read the meta data in 'chunks' to when Stream = True (in bytes)
                f.write(chunk)
                # Writes to file - Dont fully understand why you need to define the local var = 'chunk' and do this???

"""
# 5: Run cmd to execute shell
def run_cmd(command):
    subprocess.run(command, shell=True, check=True) # Dont fully understand this bit???
    # Run command in the shell if no error codes are returned?
    return 
"""

"""
# 6: Install Requests Package
def install_pkg(pkg_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
    # Why do you need to add an argument in the funtion if you are going pass it, when you call the function???
"""

# 5: Run command to install file in Windows Powershell
def run_cmd(command):
    try:
        # Run powershell cmd
        subprocess.run(["powershell", "-command", command], check=True)
        print(f"{file_name} installed sucessfully.")
    except subprocess.CalledProcessError as e:
        print(f"{file_name} failed tp install!")


# Call Functions
download_file(url, file_name)

#run_cmd(f"sudo dpkg -i {file_name}")
#run_cmd(f"sudo apt-get install -y {file_name}")

run_cmd(f"Start-Process -FilePath {file_name} -Verb RunAs -Wait") # Input Run command to Powershell

#install_pkg("requests")
