import sys
import socket

# THE BRAIN: A Dictionary of common ports
# Logic: {Port_Number: "Service_Name"}
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

print("Starting scanner...")

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
    
    # Scan ports 20 to 100 (Expanded range to catch more stuff)
    for port in range(20, 100):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5) # Speed up the timeout (0.5s) so scans are faster
            result = s.connect_ex((target, port))
            
            if result == 0:
                # LOOKUP: Get the name from our dictionary. 
                # If not found, default to "Unknown Service"
                service_name = common_ports.get(port, "Unknown Service")
                
                print(f"Port {port} ({service_name}) is open")

else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")