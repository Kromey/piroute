

def ip2int(ip):
    ip = ip.split('.')

    # Convert each octet to an integer, shift it appropriately, and sum them
    ip_int = (int(ip[0]) << 24) + (int(ip[1]) << 16)
    ip_int += (int(ip[2]) << 8) + int(ip[3])

    return ip_int
