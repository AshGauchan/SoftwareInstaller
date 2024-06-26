import os

os.environ["ENV_VAR"] = "C:\\Users\\ashim\\Downloads\\"

new_path = "C:\\Users\\ashim\\Downloads\\"

# print("Environment Variable:", os.environ["ENV_VAR"])

os.environ["PATH"] += os.pathsep + new_path

print(os.environ["PATH"])

