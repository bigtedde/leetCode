# Ted Lawson
from typing import List


def main():
    nums = [1, 2, 3, 4, 5, 1]
    flag = containsDuplicate(nums)
    print(flag)


def containsDuplicate(nums: List[int]) -> bool:
    dict1 = {}

    for num in nums:
        if num in dict1.keys():
            return True
        else:
            dict1[num] = 1

    return False


if __name__ == "__main__":
    main()
