import ipaddress
def ip_to_int32(ip: str) -> int:

    ip = ipaddress.IPv4Address(ip)
    return int(ip)


print(ip_to_int32("128.114.17.104"))