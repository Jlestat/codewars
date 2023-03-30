def xo(s: str) -> bool:
    if s.lower().count('x') == s.lower().count('o'):
        return True
    else:
        return False