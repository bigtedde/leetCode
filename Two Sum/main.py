# Ted Lawson 8/1/22
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:

        size = len(nums)

        # Add every element in the list to every other element in the list and see if the sum equals the target
        for n in range(size):
            for m in range(size):
                if (nums[n] + nums[m]) == target:
                    print(f'Target {target} found from adding values {nums[n]} + {nums[m]} at indices ({n},{m})')
                    return [n, m]


def main():
    # Initialize variables
    nums = [1, 2, 3, 4, 5, 6]
    a = Solution()

    # Test known solutions
    assert a.two_sum([1, 8, 32, 0, 4], 4) == [3, 4]
    assert a.two_sum([2, 10], 12) == [0, 1]
    assert a.two_sum([1, 2, 30], 32) == [1, 2]
    assert a.two_sum([-1, 2, 3], 1) == [0, 1]

    return a.two_sum(nums, 11)


if __name__ == '__main__':
    main()
