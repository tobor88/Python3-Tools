import sys, socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = str(input("IPv4 address of target: "))

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
valid_ip(ip)

# Connect to port
def port_connect(ip, port):
    try:
        s.connect((ip, port))
        return True
    except:
        return None

# Check port range
for port in range(1, 10000):
    value = port_connect(ip, port)
    if value == None:
        pass
    else:
        print("Port {} is open".format(port))
        break
