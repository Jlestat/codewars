def cube_odd(arr):
    result = 0
    for i in arr:
        if type(i) != int:
            return None
        else:
            if i ** 3 % 2 == 1:
                result += i ** 3
    return result


print(cube_odd([1, 2, 3, 4]))