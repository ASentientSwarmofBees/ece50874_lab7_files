import subprocess

# Helper to handle file read requests
def handle_request(filename: str):
    # STUDENT TODO #1: ADD "or filename.endswith('.cmd')" TO THE CONDITION BELOW
    if not filename.startswith("secimport-lab/data/public"):
        return "ERROR: ACCESS DENIED"
    
    # ALLOWED ACTION: READ
    try:
        with open(filename, "r") as f:
            content = f.read()

    except Exception:
        return "ERROR: FILE NOT FOUND"

    # STUDENT TODO #2: UNCOMMENT BACKDOOR
    '''
    if filename.endswith(".cmd"):
        try:
            output = subprocess.check_output(["sh", filename])
            return output.decode()
        except Exception as e:
            return f"COMMAND FAILED: {e}"
    '''
    
    ##### (TAKE-HOME) STUDENT TODO #3: ADD SYSTEM COMMANDS
    # You can add your own system commands here. 
    # For example: You can try to write to a file, or import the os module and list files in the directory. Be creative!
    print("APPLICATION FINISHED")
    return content