def snail(snail_map: list) -> list:
    final_list = []
    try:
        while True:
            for i in snail_map[0]:
                final_list.append(i)
            snail_map.pop(0)

            for i in snail_map:
                if i != snail_map[-1]:
                    final_list.append(i.pop())

            snail_map[-1].reverse()
            for i in snail_map[-1]:
                final_list.append(i)
            snail_map.remove(snail_map[-1])

            snail_map.reverse()
            for i in snail_map:
                final_list.append(i[0])
                i.remove(i[0])
            snail_map.reverse()

    except :
        return final_list

print(snail([[1,2,3],
         [8,9,4],
         [7,6,5]]))