import sys, socket

class PortScanner:
    def __init__(self, ip, ports):
        self.ip = ip
        self.ports = ports

    def scan_tcp_port(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        yield s.connect_ex((self.ip, port)), port
        s.close()

    def scan_ports(self):
        for port in self.ports:
            yield from self.scan_tcp_port(port)

    def host_up(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect_ex((self.ip, 80))
            return True
        except socket.timeout:
            return True
        except socket.error:
            return False


def main(ip, ports=range(1, 65536)):
    message = """
============================================================================
|  OSBORNEPRO                                                              |
============================================================================
Scanning IP Address for open ports. Only open ports will be displayed.
All ports are scanned by default (1-65535)
"""
    print(message)

    scanner = PortScanner(ip, ports)
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
