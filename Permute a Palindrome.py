def permute_a_palindrome(input: str) -> bool:
    if len(input) % 2 == 0:
        if len(input) // 2 == len(set(input)) or len(set(input)) == 1:
            return True
    else:
        if (len(input) // 2) + 1 == len(set(input)) or len(set(input)) == 1 or len(set(input)) % 2 == 0:
            return True
    return False


print(permute_a_palindrome('alznmgm'))