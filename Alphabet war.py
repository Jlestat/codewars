def alphabet_war(fight: str) -> str:
    
    left_side = 0
    right_side = 0
    for i in fight:
        if i == 'w':
            left_side += 4
        elif i == 'p':
            left_side += 3
        elif i == 'b':
            left_side += 2
        elif i == 's':
            left_side += 1
        elif i == 'm':
            right_side += 4
        elif i == 'q':
            right_side += 3
        elif i == 'd':
            right_side += 2
        elif i == 'z':
            right_side += 1
    if left_side > right_side:
        return 'Right side wins!'
    elif right_side > left_side:
        return 'Left side wins!'
    else:
        return 'Let's fight again!'
