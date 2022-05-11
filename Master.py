# Master Computer

import time
import socket
import sys
import os
s = socket.socket()
host socket.gethostname()
port = 8880
s.bind('', port)
s.Listen()
conn, addr = s.accept()
print.(addr, "Ls connected to server")
command = Input (str("Enter Command :"))
conn.send(command.encode())
print("Command has been sent successfully.")
data = conn.recv(1024)
if data:
    print("command received and executed successfully.")