# solution
def longest_palindrome_substr(s):
    # start from the middle and move outwards
    def _helper(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    result = ""
    n = len(s)

    for i in range(n):
        # check for the odd length
        test = _helper(i, i)
        if len(test) > len(result):
            result = test

        # check for the even length
        test = _helper(i, i + 1)
        if len(test) > len(result):
            result = test

    return result


if __name__ == "__main__":
    _s = "aa"
    _result = longest_palindrome(_s)
    print(_result)
