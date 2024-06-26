# 1 Test

from urllib.request import urlretrieve

url = ("https://central.github.com/deployments/desktop/desktop/latest/win32") # tuple i.e. immutable

file_name = "GitHubDesktopSetup-x64.exe"# File Name gotten from above link

file_path = "Downloads" # Save exe. to Downloads folder

# 3: Check meta data of the URL
path, headers = urlretrieve(url, file_name)
    # urlretrieve returns 2 values i.e. path, headers
for name, value in headers.items():
    print(name, value)


"""
Output of above code provides key data needed:
    - File saved to: GitHubDesktopSetup-x64.exe
    - Content-Length: 159078872 (~159 MB)
    - Content-Type: application/octet-stream (i.e. Binary File)
"""