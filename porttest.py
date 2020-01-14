# -*- coding: utf-8 -*-
import socket
import sys


# Ensure IPv4 address is valid
def valid_ip(ip):
    if ip.count(".") != 3:
        return False
        sys.exit(1)
    elif ip == "":
        return False
        sys.exit(1)
    else:
        split_ip = ip.split(".")
        slice_ip = [int(n) for n in split_ip[1:]]
        head = slice_ip[0]
        return all(u >= head for u in slice_ip)


# Connect to port
def port_connect(ip, port):
    try:
        s.connect((ip, port))
        return True
    except:
        return None


# The below function can be used for testing ports in a range
def check_ports():
    for port in range(1, 10000):
        # print("Testing port {}".format(port))
        value = port_connect(ip, port)
        if value is None:
            pass
        else:
            print("Port {} is open".format(port))
            sys.exit(1)


# The below function is used for testing whether or not a single port is open.
def check_port(port):
    result = port_connect(ip, port)
    if result is None:
        print("Port {} is closed".format(port))  # Replace this with pass
    else:                                        # when you scan a port range
        print("Port {} is open".format(port))
        sys.exit(1)


def main():
    valid_ip(ip)
    check_port(port)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = str(input("IPv4 address of target: "))
port = int(input("Enter port number to test: "))

main()
