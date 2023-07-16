import math

def cup_volume(d1, d2, height):
    d = (d1 + d2) / 2
    n = (math.pi * (d ** 2))/ 4 * height
    return round(n, 2)


print(cup_volume(5, 12, 31))