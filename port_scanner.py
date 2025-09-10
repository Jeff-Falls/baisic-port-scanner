
import socket

# Ask the user for the target IP address
target = input("Enter the IP address to scan: ")

# Define the range of ports to scan
start_port = 1
end_port = 1024

# Loop through each port in the range
for port in range(start_port, end_port + 1):
    # Establish what kind of address and communication protocol to use
    # (from copilot) Create a socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # Set timeout to half a second
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()
