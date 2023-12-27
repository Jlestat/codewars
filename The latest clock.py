from itertools import permutations
def late_clock(*digits):
    perms = permutations(digits)
    max_time = None
    for h1, h2, m1, m2 in perms:
        hour = h1 * 10 + h2
        minute = m1 * 10 + m2

        if hour < 24 and minute < 60:
            current_time = f"{hour:02}:{minute:02}"
            if max_time is None or current_time > max_time:
                max_time = current_time

    return max_time