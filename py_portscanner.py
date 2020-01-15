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
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        yield s.connect_ex((self.ip, port)), port
        s.close()

        
    def check_port(port):  # Test for a single open port
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
        for port in self.ports:
            yield from self.scan_tcp_port(port)

            
    def host_up(self):  # Check whether or not the host is up
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect_ex((self.ip, 80))
            return True
        except socket.timeout:
            return True
        except socket.error:
            return False

    def parseports(ports):  # syntax: port,port-range
        if not re.match(r'[\d\-,\s]+', ports):
            raise ValueError('Invalid port string')
        portstring = []
        ports = list(filter(None, ports.split(',')))
        for port in portstring:
            if '-' in port:
                try:
                    port = [int(p) for p in portstring.split('-')]
                except ValueError:
                    raise ValueError('Are you trying to scan a negative port?')
                for p in range(port[0], port[1]+1):
                    ports.append(p)
            else:
                ports.append(int(port))
        for port in portstring:
            if not (-1 < port < 65536):
                raise ValueError('Ports must be between 0 and 65535')
            return tuple(set(portstring))
        
def main(ipv4, *args):  # Main function
    """This is the main function that is used in combine the other created functions."""
    message = """
============================================================================
|  OSBORNEPRO                                                              |
============================================================================
Scanning IP Address for open ports. Only open ports will be displayed.
All ports are scanned by default (1-65535).
"""
    print(message)
    
    ports = parseports(ports)
    scanner = PortScanner(ipv4, ports)
    
    if not scanner.valid_ip(host):
        print("A valid ipv4 address was not defined. Checking for connectivity... ")
        if not scanner.host_up():
            print("Host is down. Exiting... ")
            sys.exit(1)
        else:
            print("{} is accessible ".format(host))
        

    for s, port in scanner.scan_ports():
        if s == 0:
            print(f"[*] Port {port} is OPEN")
        else:
            pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        ip = sys.argv[1]
        ports = ("9,20-23,25,37,41,42,53,67-70,79-82,88,101,102,107,109-111,"
        "113,115,117-119,123,135,137-139,143,152,153,156,158,161,162,170,179,"
        "194,201,209,213,218,220,259,264,311,318,323,383,366,369,371,384,387,"
        "389,401,411,427,443-445,464,465,500,512,512,513,513-515,517,518,520,"
        "513,524,525,530,531,532,533,540,542,543,544,546,547,548,550,554,556,"
        "560,561,563,587,591,593,604,631,636,639,646,647,648,652,654,665,666,"
        "674,691,692,695,698,699,700,701,702,706,711,712,720,749,750,782,829,"
        "860,873,901,902,911,981,989,990,991,992,993,995,8080,2222,4444,1234,"
        "12345,54321,2020,2121,2525,65535,666,1337,31337,8181,6969")
    if len(sys.argv) == 2:
        ip = sys.argv[1]
        ports = ''.join(sys.argv[2:]
        main(ip,ports)

main()
