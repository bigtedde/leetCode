# Ted Lawson
from typing import List


def main():
    testcase = [1, 2, 3, 4]
    permute(testcase)
    return


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    # base case
    if len(nums) == 1:
        print(f"BASE CASE: returning {nums[0]}")
        return [nums.copy()]

    for i in range(len(nums)):
        n = nums.pop(0)
        print(f"POP'd off {n}, starting perm")
        perms = permute(nums)

        for perm in perms:
            print(f"APPENDING {n} to this perm")
            perm.append(n)

        print(f"EXTENDING result with {perms}")
        result.extend(perms)

        print(f"UN-POPING {n}")
        nums.append(n)

    print(f"RETURNING final result: {result}")
    return result


if __name__ == "__main__":
    main()
