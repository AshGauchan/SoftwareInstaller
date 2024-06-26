import os, subprocess, time, winreg

def add_path(new_path):
    current_path = os.environ.get("PATH", "") # GET Path var's
    
    if new_path in current_path: # Check if new path exists 
        print(f"{new_path} is already in Environment Variable Path!")
        time.sleep(6)
    else:
        print(f"{new_path} added to Environment Variable Path.")
        time.sleep(6)
        return

    new_path_var = current_path + os.pathsep + new_path # Construct the new var path

    os.environ["PATH"] = new_path_var # Set new path created

    # Use setx to add path to environment variable - permenantly
    try: 
        subprocess.run(["setx", "PATH", new_path_var], check=True)
        print(f"Success! {new_path} added to Path.")
        time.sleep(6)
    except subprocess.CalledProcessError as e:
        print(f"Failed to add path to {e}!")
        time.sleep(6)


# Call Func

new_path = "C:\\Users\\ashim\\Downloads\\"

add_path(new_path)
