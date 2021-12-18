def is_palindrome(x:int):
    if x < 0:
        return False

    def _reverse_integer(x):
        import math
        res = 0
        while x > 0:
            res = res * 10 + (x % 10)
            x = math.floor(x / 10)
        return res
    return x == _reverse_integer(x)



n = 212
print(is_palindrome(n))