def highest_rank(arr: list) -> int:
    return sorted(arr,key=lambda i: (arr.count(i),i))[-1]


