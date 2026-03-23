import sys
from request_helper import handle_request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <filename>")
        sys.exit(1)

    # Simulates user input
    request = sys.argv[1]

    # Go through our dependency chain to handle the request
    with open(request, "r") as f:
        request = f.read().strip()
        response = handle_request(request)
        print(response)
