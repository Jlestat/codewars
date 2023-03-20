def is_valid_IP(strng: str) -> bool:
    ip_list = [i for i in strng.split('.')]
    for i in ip_list:
        if i.isdigit() == False or len(ip_list) != 4:
            return False
        elif i[0] == '0' and len(i) > 1 or int(i) > 255:
            return False
    return True



