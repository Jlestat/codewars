def fibs_fizz_buzz(n):
    res = []
    a = 1
    b = 1
    for i in range(n):
        if a % 5 == 0 and a % 3 == 0:
            res.append('FizzBuzz')
        elif a % 5 == 0:
            res.append('Buzz')
        elif a % 3== 0:
            res.append('Fizz')
        else:
            res.append(a)
        a, b = b, a + b
    return res


print(fibs_fizz_buzz(10))