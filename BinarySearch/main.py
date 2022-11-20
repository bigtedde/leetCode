# Ted Lawson
from typing import List


def main():
    nums = [1, 2, 3, 4, 5, 6]
    target = 6

    assert search(nums, target) == 5

    print(search(nums, target))

    return


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        pivot = (left + right) // 2

        if nums[pivot] < target:
            left = pivot + 1

        else:
            right = pivot

    if nums[left] == target:
        return left
    else:
        return -1


if __name__ == "__main__":
    main()
