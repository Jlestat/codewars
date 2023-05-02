def remove_smallest(numbers: list) -> list:
    new_list = numbers[:]
    try:
        new_list.remove(min(new_list))
        return new_list
    except:
        return []


print(remove_smallest([1, 2, 3, 4, 5]))

