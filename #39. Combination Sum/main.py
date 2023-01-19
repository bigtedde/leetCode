# Ted Lawson on 1/19/23
from typing import List


def main():
    candidates = [2, 3, 6, 7, 9, 5]
    target = 10
    a = Solution().combinationSum(candidates, target)
    print(f"The final answer is: {a}")
    return

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        # method to preform depth first search
        def dfs(index: int, subset: List[int], value: int):
            if value == target:
                print(f"Found a new combination that adds to {target}: {subset}")
                answer.append(subset[:])
                return
            if index == len(candidates) or value > target:
                print(f"COMBO FAILED: value of {value}, or out of range")
                return

            # Recursively add this index and increment value
            print(f"APPENDING {candidates[index]} to {subset}")
            subset.append(candidates[index])
            dfs(index, subset, value + candidates[index])

            # Recursively add the rest of the candidates
            print(f"POPING {candidates[index]} from  {subset}")
            subset.pop()
            dfs(index + 1, subset, value)

        dfs(0, [], 0)
        return answer


if __name__ == "__main__":
    main()
