def longest_common_prefix(strs: list):
    longest = ""

    if len(strs) == 0:
        return longest

    comp_word = strs[0]
    comp_index = 0

    for comp_letter in comp_word:
        for current_word in strs[1:]:
            if comp_index >= len(current_word):
                return longest
            current_letter = current_word[comp_index]
            if comp_letter != current_letter:
                return longest
        comp_index += 1
        longest += comp_letter

    return longest


# strs = ["flower", "flight", "fly"]
strs = ["ab", "a"]
print(longest_common_prefix(strs))
