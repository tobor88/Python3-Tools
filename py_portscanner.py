# -*- coding: utf-8 -*-
import socket
import sys


class PortScanner:
    def __init__(self, ip, ports):  # Define objects properties
        """This of course defines the properties of the object."""
        self.ip = ip
        self.ports = ports


    def valid_ip(ip):  # Validate the ipv4 address given is valid
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
        
        
    def scan_tcp_port(self, port):  # Create socket for connectin to ports and issue connect
        """This function creates the socket and connects to it."""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        yield s.connect_ex((self.ip, port)), port
        s.close()

        
    # The below function is used for testing whether or not a single port is open.
    def check_port(port):
        def port_connect(ip, port):
            try:
                s.connect((ip, port))
                return True
            except:
                return None
        result = port_connect(ip, port)
        if result is None:
            print("Port {} is closed".format(port))  # Replace this with pass
        else:                                        # when you scan a port range
            print("Port {} is open".format(port))
            sys.exit(1)
        
        
    def scan_ports(self):  # Connect to all ports in the range
        """This function connects to all ports in the range."""
        for port in self.ports:
            yield from self.scan_tcp_port(port)

            
    def host_up(self):  # Check whether or not the host is up
        """Verifies the target host is accessible by testing a connection to port 80."""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect_ex((self.ip, 80))
            return True
        except socket.timeout:
            return True
        except socket.error:
            return False


def main(ipv4, ports=range(1, 65536)):  # Main function
    """This is the main function that is used in combine the other created functions."""
    message = """
============================================================================
|  OSBORNEPRO                                                              |
============================================================================
Scanning IP Address for open ports. Only open ports will be displayed.
All ports are scanned by default (1-65535).
"""
    print(message)

    scanner = PortScanner(ipv4, ports)
    if not scanner.host_up():
        print("Host is down")
        return

    for s, port in scanner.scan_ports():
        if s == 0:
            print(f"[*] Port {port} is OPEN")
        else:
            pass


if __name__ == '__main__':
    if len(sys.argv) == 2:
        ip = sys.argv[1]
        main(ip)

main()
