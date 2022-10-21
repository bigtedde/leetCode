# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    n = 5
    bad = 4

    def isBadVersion(self, n: int) -> bool:

        if n >= self.bad:
            return True
        else:
            return False

    def firstBadVersion(self, n: int) -> int:

        lower, upper, mid = 1, n, (1 + n) // 2
        print(f'Checking {lower}, {upper}, {mid}')

        while upper > lower:
            print(f'Checking {lower}, {upper}, {mid}')

            if self.isBadVersion(mid):
                upper = mid
                mid = (lower + upper) // 2
            else:
                lower = mid + 1
                mid = (lower + upper) // 2

        if self.isBadVersion(lower):
            print(lower)
            return lower
        else:
            print(upper)
            return upper

