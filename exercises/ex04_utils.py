"""list Utility Functions."""

__author__ = "730621008"


def all(nums: list[int], match: int) -> bool:
    for num in nums:
        if num != match:
            return False
    return True if nums else False


def max(nums: list[int]) -> int:
    if len(nums) == 0:
        raise ValueError("max() arg is an empty List")
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    for num in list2:
        list1.append(num)