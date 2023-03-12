def queue_time(customers, n):
    new_list = [0]*n
    for i in customers:
        new_list[0] += i
        new_list.sort()
    return max(new_list)




