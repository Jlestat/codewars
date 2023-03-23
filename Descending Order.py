def descending_order(num):
    new_list = [int(i) for i in str(num)]
    new_list.sort(reverse=True)
    new_list = int(''.join(map(str, new_list)))
    return new_list


