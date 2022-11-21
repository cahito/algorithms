def order_word(word: str):
    n = len(word)
    if n == 1:
        return word
    for ordered_chars in range(n - 1):
        for idx in range(0, n - 1 - ordered_chars):
            if word[idx] > word[idx +1]:
                curr_idx = word[idx]
                print("curr_index", curr_idx)
                word.replace(word[idx], word[idx +1], 1)
                word.replace(word[idx + 1], curr_idx, 1)
    print(word)
    return word


def is_anagram(first_string: str, second_string:str):
    if first_string == "" or second_string == "":
        return (first_string, second_string, False)
    first_ordered = order_word(first_string.casefold())
    print(first_ordered)
    second_ordered = order_word(second_string.casefold())
    print(second_ordered)

    return (first_ordered, second_ordered, first_ordered == second_ordered)
