import socket
import subprocess

# Helper to handle file read requests
def handle_request(action: str, target: str):
    if action == "READ":
        # STUDENT TODO #1: ADD "or filename.endswith('.cmd')" TO THE CONDITION BELOW
        if not target.startswith("secimport-lab/data/public"):
            return "ERROR: ACCESS DENIED"
        
        # STUDENT TODO #2: UNCOMMENT BACKDOOR
        '''
        if filename.endswith(".cmd"):
            try:
                output = subprocess.check_output(["sh", filename])
                content = output.decode()
            except Exception as e:
                return f"COMMAND FAILED: {e}"
        '''

        try:
            with open(target, "r") as f:
                content = f.read()
    
        except Exception:
            return "ERROR: FILE NOT FOUND"
    

    # COMMANDS FOR TAKE-HOME LAB

    # WRITE (Tests Syscall Arguments)
    elif action == "WRITE":
        # STUDENT TODO #3: Restrict 'openat' to only allow writing to /tmp/
        with open(target, "w") as f:
            f.write("Log entry at " + str(time.time()))
        return f"SUCCESS: Wrote to {target}"
    
    # CONNECT (Tests Syscall Arguments, Syscall Ordering)
    elif action == "CONNECT":
        # STUDENT TODO #4: Restrict 'connect' to only allow connecting to 127.0.0.1
        # STUDENT TODO #5: Restrict 'connect' to not be allowed after any READ has taken place, to prevent sensitive information from being sent to an attacker's server
        try:
            host, port = target.split(":")
            port = int(port)
            
            # This triggers: socket(), connect()
            with socket.create_connection((host, port), timeout=2) as sock:
                return f"SUCCESS: Connected to {host} on port {port}"
        except Exception as e:
            return f"CONNECTION FAILED: {e}"

    
    print("APPLICATION FINISHED")
    return content