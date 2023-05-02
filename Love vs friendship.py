def words_to_marks(s: str) -> int:
    final_sum = 0
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in s:
        final_sum += letters.index(i) + 1
    return final_sum


print(words_to_marks('attitude'))