# from typing import List


def find_duplicate(nums: list):
    if len(nums) == 0 or len(nums) == 1:
        return False

    # ordered_nums = order_word(nums)
    nums.sort()

    n = len(nums) - 1
    x = 0
    while x < n:
        if type(nums[x]) != int or nums[x] < 0:
            return False
        if nums[x] == nums[x + 1]:
            return nums[x]
        x += 1

    return False
