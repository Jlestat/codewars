def maskify(cc: str) -> str:
    if len(cc) <= 4:
        return cc
    else:
        return (len(cc) - 4) * '#' + cc[-4:]



print(maskify('4556364607935616'))