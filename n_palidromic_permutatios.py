MAX = 256

# Returns factorial of n
def fact(n):
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res


# returns count of palindromic permutations of str.
def count_palin_permutations(string):
    global MAX

    # count frequencies of all characters
    n = len(string)
    freq = [0] * MAX
    for i in range(n):
        freq[ord(string[i])] = freq[ord(string[i])] + 1

    # Since half of the characters decide count of palindromic permutations, we take (n/2)!
    res = fact(int(n/2))

    # To make sure that there is at most one odd occuring char
    odd_freq = False

    # Traverse through all counts
    for i in range(MAX):
        half = int(freq[i] / 2)
        # to make sure that the string can permute to form a palindrome
        if freq[i] % 2 != 0:

            # If there are more than one odd occuring chars
            if odd_freq == True:
                return 0

            odd_freq = True

        # Divide all permutations with repeated characters
        res = int(res / fact(half))

    return res


if __name__== "__main__":
    _string = "gffg"
    res = count_palin_permutations(_string)
    print(res)