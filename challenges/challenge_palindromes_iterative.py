def is_palindrome_iterative(word):
    array = list(word)
    if len(array) == 0:
        return False
    n = len(array) - 1
    x = 0
    while x <= n:
        if array[x] != array[n]:
            return False
        x += 1
        n -= 1

    return True
