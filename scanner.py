import sys
import socket

print ("starting scanner...")

#logic
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
    # Scan ports 50 to 85
    for port in range(50, 85):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            
            if result == 0:
                print(f"Port {port} is open")

else:
    print ("Invalid amount of arguments.")
    print ("Syntax:python3 scanner.pi <ip>")
