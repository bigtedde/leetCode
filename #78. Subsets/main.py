# Ted Lawson
from typing import List


def main():
    nums = [1, 2, 3, 4]
    answer = Solution().subsets(nums)
    print(f"final answer: {answer}")
    return 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []

        def dfs(index: int):

            if index == len(nums):
                print(f"ADDING ENTRY TO FINAL RESULTS: {subset}")
                results.append(subset[:]) # setset[:] == subset.copy(), more efficient
                return

            print(f"APPENDING {nums[index]} to {subset}")
            subset.append(nums[index])
            dfs(index + 1)

            print(f"POPING {nums[index]} from {subset}")
            subset.pop()
            dfs(index + 1)

        dfs(0)
        return results


if __name__ == "__main__":
    main()
