def two_oldest_ages(ages: list) -> list:
    final_list = []
    final_list.append(max(ages))
    ages.remove(max(ages))
    final_list.append(max(ages))
    return sorted(final_list)


print(two_oldest_ages([1, 5, 87, 45, 8, 8]))