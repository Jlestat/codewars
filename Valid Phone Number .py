import re
def valid_phone_number(phoneNumber: str) -> bool:
    s = re.compile(r'^\(\d{3}\)\s\d{3}\-\d{4}$')
    result = s.match(phoneNumber)
    return bool(result)