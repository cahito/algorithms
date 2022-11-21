def order_word(word: list):
    n = len(word) - 1
    if n == 0:
        return word
    x = 0
    while x < n:
        temp_array = word[x:]
        curr_first = temp_array[0]
        idx_min = temp_array.index(min(temp_array))
        word[x] = temp_array[idx_min]
        word[idx_min + x] = curr_first
        x += 1

    return word


def is_anagram(first_string: str, second_string: str):

    # método list() encontrado no site:
    # https://www.digitalocean.com/community/tutorials/python-convert-string-to-list

    first_array = list(first_string.casefold())
    first_ordered = order_word(first_array)

    first_result = "".join(first_ordered)

    second_array = list(second_string.casefold())
    second_ordered = order_word(second_array)

    second_result = "".join(second_ordered)

    if first_result == "" and second_result == "":
        return (first_result, second_result, False)

    return (first_result, second_result, first_result == second_result)
