def mineLocation(field: list) -> list:
    final_list = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                final_list.append(i)
                final_list.append(j)
                break
    return final_list


print(mineLocation([ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0] ]))