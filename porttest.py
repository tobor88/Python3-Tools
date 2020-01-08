import socket

ip = str(input("Enter the ip: "))

try:
    socket.inet_aton(ip)
except socket.error as msg:
    print("A valid ipv4 address was not defined {}".format(msg)) # This may need to be changed to + str(msg) depending on your python3 version

port = int(input("Enter the port: "))
# Validate port value
def test_port(n):
    if n in range(1, 65535):
        print()
    else:
        print("A valid port number was not specified")
 
test_port(port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if s.connect((ip, port)):
   print("Port " + port + " is closed. BUMMER")
else:
   print("Port " + port + " is open. HOORAY!")
