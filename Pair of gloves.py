import collections
def number_of_pairs(gloves: list) -> int:
    cur_coll = collections.Counter(gloves)
    sum_of_pairs = 0
    for i in cur_coll.values():
        if i >= 2:
            sum_of_pairs += i // 2

    return sum_of_pairs


print(number_of_pairs(["red","red"]))