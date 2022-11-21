# from typing import List


def find_duplicate(nums: list):
    if len(nums) == 0 or len(nums) == 1:
        return False

    # ordered_nums = order_word(nums)
    n = len(nums) - 1
    x = 0
    while x <= n:
        temp_array = nums[x:]
        curr_first = temp_array[0]
        if type(curr_first) != int or curr_first < 0:
            return False
        idx_min = temp_array.index(min(temp_array))
        nums[x] = temp_array[idx_min]
        nums[idx_min + x] = curr_first
        if nums[x] in nums[x + 1:]:
            return nums[x]
        x += 1

    return False
