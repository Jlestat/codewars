def parse(data: str) -> list:
    final_list = []
    start_number = 0
    for i in data:
        if i == 'i':
            start_number += 1
        elif i == 'd':
            start_number -= 1
        elif i == 's':
            start_number **= 2
        elif i == 'o':
            final_list.append(start_number)

    return final_list


print(parse('idoiido'))