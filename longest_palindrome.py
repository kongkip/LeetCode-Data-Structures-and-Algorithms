def longest_palindrome(s):
    counts = {}

    for c in s:
        counts[c] = counts.get(c, 0) + 1
    print(counts)
    
    result, odd_found = 0, False
    for _, c in counts.items():
        if c % 2 == 0:
            result += c 
        else:
            odd_found = True
            result += c - 1
    if odd_found:
        result += 1
    return result


if __name__ == "__main__":
    s = "babad"
    _result = longest_palindrome(s)
    print(_result)
