import socket

ip = str(input("Enter the ip: "))
port = int(input("Enter the port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if s.connect((ip, port)):
   print("Port " + port + " is closed. BUMMER")
else:
   print("Port " + port + " is open. HOORAY!")
