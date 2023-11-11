def solve(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            new_str = s[i:j+1]
            if int(new_str) % 2 != 0:
                count += 1
    return count