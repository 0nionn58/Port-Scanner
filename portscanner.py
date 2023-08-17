#!/bin/python3

import socket
import sys
from datetime import datetime
file_path = "common_ports.txt"
with open(file_path, "r") as file: #Get most common ports
    CommonPorts = file.read()
CommonPorts = (CommonPorts.replace("\n", " ")).split()

error_displayed = False
target = "none"
ports_open = []
help_flags = ["-h", "--help"]
#Define our target
try:
    if len(sys.argv) != 2:
        print("Invalid amount of arguments")
        print("Syntax: portscanner.py <ip>")
        sys.exit()
    for argument in sys.argv:
        if argument in help_flags:
            print("Syntax: portscanner.py <ip>")
            sys.exit()
    else:
        target = socket.gethostbyname(sys.argv[1]) #Translate host name to IPV4
except socket.gaierror:
    if not error_displayed:
        print("Please input a valid hostname or IP")
        error_displayed = True
    sys.exit()
#------------------------------------------------------------------------------------------------------
#Add pretty banner
print("- " * 50)
print("Scanning target: " + target)
start_time = datetime.now()
print("Starting portscanner at " + str(start_time))
print("- " * 50)
#------------------------------------------------------------------------------------------------------
try:
    for port in CommonPorts:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, int(port))) #returns error indicator (0: open 1: closed)
        if result == 0:
            ports_open.append(port)
            print("Port {port} is open".format(port = port))
        else:
            #print("Port {port} is not open".format(port = port))
            pass
except KeyboardInterrupt:
    print("\nScan aborted by user.")
except Exception as e:
    print("An error occurred: ", e)
    sys.exit()
#------------------------------------------------------------------------------------------------------
#If no ports are open
if ports_open == []:
    print("No common ports open")
#------------------------------------------------------------------------------------------------------
#calculate time taken
end_time = datetime.now()
time_taken = end_time - start_time
print("_ " * 50)
print("Time elapsed: " + str(time_taken))
#------------------------------------------------------------------------------------------------------

