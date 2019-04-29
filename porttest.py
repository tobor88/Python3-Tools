#!/usr/bin/python
import socket
ip = raw_input("Enter the ip: ")
port = input("Enter the port: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect_ex((ip, port)):
   print "Port", port, "is closed. BUMMER :("
else:
   print "Port", port, "is open. HOORAY!"
