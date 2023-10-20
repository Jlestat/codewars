from datetime import date


def to_day_of_year(dat: list) -> int:
    d = dat[0]
    m = dat[1]
    y = dat[2]
    return (date(y, m, d) - date(y, 1, 1)).days + 1


print(to_day_of_year([25, 12, 2017]))
