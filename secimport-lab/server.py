import sys
from request_helper import handle_request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <filename>")
        sys.exit(1)

    # Simulates user input
    request_file = sys.argv[1]

    # Go through our dependency chain to handle the request
    try:
        with open(request_file, "r") as f:
            # Iterate through each line in the request file
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith("#"): # Skip empty lines or comments
                    continue
                
                # Split into ACTION and TARGET (e.g., "READ public.txt")
                parts = line.split(" ", 1)
                if len(parts) < 2:
                    print(f"Line {line_num}: Skipping invalid format.")
                    continue
                
                action, target = parts
                print(f"--- Processing Request {line_num}: {action} on {target} ---")
                
                # Call the helper
                response = handle_request(action, target)
                print(f"Response: {response}\n")

    except FileNotFoundError:
        print(f"Error: Request file '{request_file}' not found.")
