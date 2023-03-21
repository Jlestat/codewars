def parts_sums(ls):
    final_list = [sum(ls)]
    for i in ls:
        final_list.append(final_list[-1]-i)
    return final_list


