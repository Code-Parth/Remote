# Slave Computer

import time
import socket
import sys
import os
S = socket.socket()
host = "127.0.0.1"
port = 8080
s.connect((host, port))
print("Connected to Server.")
command = s.recv(1024)
command = command.decode()
Lf command == "open":
print("Command is ", command)
s.send("Command received". encode())
os.system('ls')