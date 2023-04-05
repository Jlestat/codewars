def sum_of_minimums(numbers: list) -> int:
    fin_sum = 0
    for i in numbers:
        fin_sum += min(i)
    return fin_sum



print(sum_of_minimums([[ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]))

