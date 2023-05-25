def get_consective_items(items: str, key: str) -> int:
    """
    :param items: str/int
    :param key: str/int
    :return: int
    """
    items = str(items)
    key = str(key)
    final_count = 0
    curr_count = 0
    if key not in items:
        return 0
    else:
        for i in range(len(str(items)) - 1):
            if items[i] == str(key) and items[i + 1] == str(key):
                curr_count += 1
            else:
                if final_count < curr_count:
                    final_count = curr_count
                    curr_count = 0
                else:
                    curr_count = 0
        if curr_count >= final_count:
            final_count = curr_count
        return final_count + 1

print(get_consective_items('555555555592222222111111111166644422222000000222222222266666666555555555888811111111113333333333555533333333351111111111111111155999999333377788888111111133333333333333999999999999944444444466666666661111110000222222222244444444445557777777', '5'))