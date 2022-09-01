# Ted Lawson 8/7/22
class Solution:
    def is_palindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l].isalnum():
                while not s[r].isalnum():
                    r = r-1
                if s[l].lower() != s[r].lower():
                    # print(s[l], " ", s[r], " failed")
                    return False
                else:
                    l += 1
                    r -= 1
            else:
                l += 1

        return True


def main():
    s = "Race......car"
    answer = Solution().is_palindrome(s)
    print(answer)
    return answer


if __name__ == "__main__":
    main()
