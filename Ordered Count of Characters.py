from collections import Counter


def ordered_count(inp: str) -> list[tuple]:
    new_list = Counter(inp)
    result = []
    for k, w in new_list.items():
        result.append((k, w))
    return result


print(ordered_count("abracadabra"))