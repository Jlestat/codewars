def ips_between(start_ip, end_ip):
    start_ip_int = sum(int(octet) << (8 * (3 - i)) for i, octet in enumerate(start_ip.split('.')))
    end_ip_int = sum(int(octet) << (8 * (3 - i)) for i, octet in enumerate(end_ip.split('.')))

    count = end_ip_int - start_ip_int

    return count




print(ips_between("10.0.0.0", "10.0.0.50"))