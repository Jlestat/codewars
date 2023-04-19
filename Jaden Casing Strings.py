import re
def to_jaden_case(string: str) -> str:
    new_str = string.split()
    s = ' '.join(new_str)
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", lambda mo: mo.group(0).capitalize(),s)


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))