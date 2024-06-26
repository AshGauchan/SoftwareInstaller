""" A """

# 1:
import os, stat

# 2: 
def check_write_perm(file):
    f_status = os.stat(file) # check file status
    f_mode = f_status.st_mode # extract's the mode (i.e. permission bits)
    has_write_perm_user = bool(f_mode & stat.S_IWUSR)

    return{
        "user_write_permission": has_write_perm_user
    }


# 3:
file = "C:\\Users\\ashim\\Downloads\\GitHubDesktopSetup-x64.exe"

perm1 = check_write_perm(file)
print(f"User write permission: {perm1["user_write_permission"]}")

""" B """

# 1
print(os.access(file, os.W_OK)) # W_OK = for writing & R_OK = for reading


