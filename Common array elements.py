from collections import Counter


def common(a: list, b: list, c: list) -> int:
    """
    :param a: first list
    :param b: second list
    :param c: third list
    :return:
    """
    list1 = Counter(a)
    list2 = Counter(b)
    list3 = Counter(c)
    keys = Counter(a+b+c).keys()
    return sum(list(map(lambda x: x * min(list1[x], list2[x], list3[x]), keys)))


print(common([1,2,2,3],[5,3,2,2],[7,3,2,2]))