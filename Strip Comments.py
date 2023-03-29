def solution(string: str, markers: list) -> str:
    split_list = string.split('\n')
    for i, line in enumerate(split_list):
        for m in markers:
            index = line.find(m)
            if index != -1:
                line = line[:index]
        split_list[i] = line.rstrip(' ')

    return '\n'.join(split_list)