
# 1: Import required modules
import sys, requests, os

# 2: Set variables
url_link = "https://central.github.com/deployments/desktop/desktop/latest/win32"
#file_path = os.chdir("Downloads")

req1 = requests.get(url_link)
# print(req.headers) #pulls meta data
# print(req.url) # pulls actual text of url
    # outputs = https://desktop.githubusercontent.com/github-desktop/releases/3.4.1-cb739340/GitHubDesktopSetup-x64.exe

file_name = req1.url[url_link.rfind("/")+16:]
#print(file_name)
    # outputs = GitHubDesktopSetup-x64.exe

# 3: Download GitHub Desktop
def download_file(url):
    try:
        if file_name:
            pass
        else:
            file_name = req1.url[url_link.rfind("/")+16:]
        with requests.req1 as req2:
            with open(file_name, "wb") as git_file:
                for file_size in req1.iter_content(chunk_size=10000):
                    if file_size:
                        git_file.write(file_name)
            return file_name
    except Exception as error_response:
        print(error_response)
        return None

download_file(url_link)