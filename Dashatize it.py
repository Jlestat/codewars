def dashatize(n):
    print(n)
    if type(n) == int:
        n = str(abs(n))
        fin_str = ""
        for e,i in enumerate(n):
            if int(i) % 2 != 0:
                if e == 0:
                    fin_str += "{}-".format(i)
                elif e == len(n)-1:
                    fin_str += "-{}".format(i)
                else:
                    fin_str += "-{}-".format(i)
            else:
                fin_str += i
        if fin_str[-1] == "-": fin_str = fin_str[:-1]
        return fin_str.replace("--", "-")
    else:
        return "None"


print(dashatize(1))