def row_weights(array):
    first_team = 0
    second_team = 0
    for i in range(len(array)):
        if (i + 1) % 2 == 0:
            second_team += array[i]
        else:
            first_team += array[i]
    return (first_team, second_team)