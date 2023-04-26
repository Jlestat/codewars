def count_smileys(arr: list) -> int:
    fin_sum = 0
    for s in arr:
        if len(s) == 2 and s[0] in [":", ";"] and s[-1] in [")", "D"]:
            fin_sum += 1
        elif len(s) > 2 and s[0] in [":", ";"] and s[1] in ["-", "~"] and s[-1] in [")", "D"]:
            fin_sum += 1
    return fin_sum


print(count_smileys([':D',':~)',';~D',':)']))