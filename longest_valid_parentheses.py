def longest_valid_parentheses(s: str):

    # stack list to keep the index of open parentheses

    stack = [-1]
    max_len = 0
    for i, p in enumerate(s):
        if p == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i-stack[-1])
    return max_len

s = "()(()"
print(longest_valid_parentheses(s))