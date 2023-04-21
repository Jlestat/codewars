def find_missing(sequence: list) -> int:
    try:
        cur_prog = []
        for i in range(len(sequence) - 1):
            cur_prog.append(sequence[i + 1] - sequence[i])
        if min(cur_prog) > 0:
            real_list = [i for i in range(min(sequence), max(sequence), min(cur_prog))]
            return list(set(real_list) - set(sequence))[0]
        else:
            real_list = [i for i in range(max(sequence), min(sequence), max(cur_prog))]
            return list(set(real_list) - set(sequence))[0]
    except:
        return 0



print(find_missing([-1, -3, -4, -5, -6, -7, -8, -9]))
