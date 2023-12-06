def data_reverse(data):
    str_data = [str(i) for i in data]
    temp = ''.join(str_data)
    res = []
    for i in range(0, len(temp), 8):
        res.append(temp[i:i + 8])
    final_res = []
    for i in res[::-1]:
        for j in i:
            final_res.append(int(j))
    return final_res


print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))