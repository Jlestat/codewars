def solution(text: str, ending: str) -> bool:
    part_of_text = text[len(text) - len(ending):]
    if ending == part_of_text:
        return True
    else:
        return False


print(solution('abc', 'bc'))