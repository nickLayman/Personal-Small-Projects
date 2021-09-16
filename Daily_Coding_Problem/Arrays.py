"""
Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.

[1, 2, 3, 4, 5] -> [120, 60, 40, 30, 24]
[3, 2, 1] -> [2, 3, 6]

Follow-up: What if you can't use division?
"""


def products(nums):
    prefixes = []
    for num in nums:
        if not prefixes:
            prefixes.append(num)
        else:
            prefixes.append(prefixes[-1]*num)

    suffixes = []
    for num in reversed(nums):
        if not suffixes:
            suffixes.append(num)
        else:
            suffixes.append(suffixes[-1]*num)
    suffixes.reverse()

    product_list = []
    for i in range(len(nums)):
        if i == 0:
            product_list.append(suffixes[i+1])
        elif i == len(nums) - 1:
            product_list.append(prefixes[i-1])
        else:
            product_list.append(prefixes[i-1]*suffixes[i+1])

    return product_list


"""
Given an array of integers that are out of order, determine the bounds
of the smallest window that must be sorted in order for the entire
array to be sorted.

[3, 7, 5, 6, 9] -> (1, 3)
[4, 5, 7, 8, 6, 9] -> (2, 4)
"""


def smallest_window(nums):
    start = 0
    end = len(nums) - 1
    max_seen = -float("inf")
    min_seen = float("inf")
    for i in range(len(nums)):
        if nums[i] < max_seen:
            end = i
        if nums[i] > max_seen:
            max_seen = nums[i]

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > min_seen:
            start = i
        if nums[i] < min_seen:
            min_seen = nums[i]

    return [start, end]


print(smallest_window([3, 7, 5, 6, 9]))
