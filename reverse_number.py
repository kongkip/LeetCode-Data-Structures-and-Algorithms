def reverse_interger(x: int):
    import math
    neg = False
    if x < 0:
        x *= -1
        neg = True

    res = 0
    while x > 0:
        res = res*10 + (x % 10)
        x = math.floor(x / 10)

    if res > 2**33 - 1:
        return 0

    return res * -1 if neg else res


n = 1245
print(reverse_interger(n))
