def open_or_senior(data: list) -> list:
    final_list = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            final_list.append('Senior')
        else:
            final_list.append('Open')
    return final_list



print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))