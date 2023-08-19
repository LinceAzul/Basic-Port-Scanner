#!/bin/python3

import sys
import socket
from datetime import datetime


# Divide each octet
targetIP = str(sys.argv[1])
octetsList = targetIP.split('.') # List of the 4 octets
for i in range(0, 4):
	if len(octetsList) != 4 or octetsList[i] == "" :
		print("Error: wrong IP address, the format is x.x.x.x")
		sys.exit()
	if int(octetsList[i]) not in range(0, 256):
		print(f"Error: IP address NOT in a valid range. ctet {i+1} = {portList[i]} not valid")
		sys.exit()

# Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

# Add a pretty banner
print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" *50)

# Add functionalities (make it do something)
try:
	for port in range(50, 85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(.5)
		result = s.connect_ex((target, port))
		if result == 0:
			print(f"Port {port} is open")
		if port == 84:
			print("End of port scanner ...")
		s.close()
except KeyboardInterrupt: # What if we hit CTRL + C
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror: # GAI error happens when the host could not be resolved
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error: # Error control
	print("Could not connect to the server.")
	sys.exit()
	

