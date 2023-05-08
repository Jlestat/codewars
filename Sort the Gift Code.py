def sort_gift_code(code: str) -> str:
    new_list = list(code)
    new_list.sort()
    return ''.join(new_list)


print(sort_gift_code('zyxwvutsrqponmlkjihgfedcba'))