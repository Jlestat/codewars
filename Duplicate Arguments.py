def solution(*args):
    new_list = [*args]
    if len(new_list) == len(set(new_list)):
        return False
    else:
        return True


