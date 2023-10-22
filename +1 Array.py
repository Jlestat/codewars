def up_array(arr: list):
    if not arr or any(x < 0 or x > 9 for x in arr):
        return None
    elif len(arr) == 1:
        str_lst = [str(numb) for numb in arr]
        int_conv = int("".join(str_lst)) + 1
        return [int(x) for x in str(int_conv)]
    elif arr[0] == 0 and arr[1] == 0:
        str_lst = [str(numb) for numb in arr]
        int_conv = int("".join(str_lst)) + 1
        res = [int(x) for x in str(int_conv)]
        res.insert(0, 0)
        res.insert(0, 0)
        return res
    elif arr[0] == 0:
        str_lst = [str(numb) for numb in arr]
        int_conv = int("".join(str_lst)) + 1
        res = [int(x) for x in str(int_conv)]
        res.insert(0, 0)
        return res

    else:
        str_lst = [str(numb) for numb in arr]
        int_conv = int("".join(str_lst)) + 1
        return [int(x) for x in str(int_conv)]


print(up_array([0, 0, 8, 5, 4, 6, 9, 5, 1, 3, 5, 1, 1, 8, 4, 9, 3, 6, 8, 1, 4]))