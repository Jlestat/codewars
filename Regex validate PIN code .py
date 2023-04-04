def validate_pin(pin: str) -> bool:
    if len(pin) == 4 or len(pin) == 6:
        for i in pin:
            if i not in '1234567890':
                return False
        else:
            return True
    else:
        return False


print(validate_pin('123456'))