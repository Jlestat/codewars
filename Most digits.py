def find_longest(arr: list) -> int:
    fin_str = ''
    for i in arr:
        if len(str(i)) > len(fin_str):
            fin_str = str(i)
    return int(fin_str)



print(find_longest([1, 10, 100]))