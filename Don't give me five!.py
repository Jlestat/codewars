def dont_give_me_five(start,end):
    final_count = 0
    for i in range(start, end + 1):
        if '5' in str(i):
            continue
        else:
            final_count += 1
    return final_count


def dont_give_me_five2(start,end):
    return len([str(i) for i in range(start, end + 1) if str(i).count('5') == 0])