def is_lucky(ticket):
    try:
        if int(ticket[3]) + int(ticket[4]) + int(ticket[5]) == int(ticket[0]) + int(ticket[1]) + int(ticket[2]):
            return True
        else:
            return False
    except Exception:
        return False