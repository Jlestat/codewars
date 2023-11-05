def triple_double(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)

    for digit in "0123456789":
        if digit * 3 in num1_str and digit * 2 in num2_str:
            return 1

    return 0