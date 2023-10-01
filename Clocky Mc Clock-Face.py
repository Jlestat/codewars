def what_time_is_it(angle):
    give_hours = int(angle // 30)
    give_minute = int((angle % 30) * 2)
    if give_hours == 0:
        give_hours = 12
    return f'{str(give_hours).zfill(2)}:{str(give_minute).zfill(2)}'