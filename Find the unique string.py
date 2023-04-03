def find_uniq(arr: list) -> str:
    if set(arr[0].lower()) != set(arr[1].lower()) and set(arr[0].lower()) != set(arr[2].lower()):
        return arr[0]
    else:
        first_str = set(arr[0].lower())
        for i in arr:
            if set(i.lower()) == first_str:
                continue
            else:
                return i



print(find_uniq([ 'b', 'a', 'a', 'a', 'a', 'a', 'a' ]))

