def is_monotone(heights: list) -> bool:
    curr_list = sorted(heights)
    str_list = [str(i) for i in curr_list]
    heights_str = [str(i) for i in heights]
    if ''.join(str_list) == ''.join(heights_str):
        return True
    else:
        return False


print(is_monotone([1,2,3]))