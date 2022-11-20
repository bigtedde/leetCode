# Ted Lawson 8/7/22
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, m, r = 0, (len(nums) - 1) // 2, len(nums) - 1

        def binary_search(self, nums: List[int], left: int, mid: int, right: int, target: int) -> int:
            if nums[mid] == target:
                return mid

            elif left < 0 or right == len(nums) or left > right or right < left:
                return -1

            elif nums[mid] < target:
                return binary_search(self, nums, mid + 1, ((mid + 1 + right) // 2), right, target)

            elif nums[mid] > target:
                return binary_search(self, nums, left, (left + mid - 1) // 2, mid - 1, target)

        return binary_search(self, nums, l, m, r, target)


def main():
    nums = [-1, 0, 3, 5, 9, 12, 13, 18, 22, 23, 24, 25, 26, 27, 29, 30]
    target = 1

    answer = Solution().search(nums, target)
    print(answer)
    return answer


if __name__ == '__main__':
    main()
