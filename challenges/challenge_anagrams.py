def order_word(word: list, x=0, n=None):
    if n is None:
        n = len(word)
    if n == 1:
        return word
    if (n - x) > 1:
        mid = (x + n) // 2
        order_word(word, x, mid)
        order_word(word, mid, n)
        word_merge(word, x, mid, n)

    """ while x < n:
        temp_array = word[x:n]
        curr_first = temp_array[0]
        curr_last = temp_array[-1]
        idx_min = temp_array.index(min(temp_array))
        idx_max = temp_array.index(max(temp_array))
        word[x] = temp_array[idx_min]
        word[n - 1] = temp_array[idx_max]
        word[idx_min + x] = curr_first
        word[idx_max - x] = curr_last
        x += 1
        n -= 1 """

    return word


def word_merge(word, x, mid, n):
    left = word[x:mid]
    right = word[mid:n]

    left_index, right_index = 0, 0

    for idx in range(x, n):
        if left_index >= len(left):
            word[idx] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            word[idx] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            word[idx] = left[left_index]
            left_index = left_index + 1
        else:
            word[idx] = right[right_index]
            right_index = right_index + 1


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
