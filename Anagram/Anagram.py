# Ted Lawson

class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        hashMapA, hashMapB = {}, {}

        for e in range(len(s)):
            hashMapA[s[e]] = 1 + hashMapA.get(s[e], 0)
            hashMapB[t[e]] = 1 + hashMapB.get(t[e], 0)

        for k in hashMapA:
            if hashMapB.get(k, 0) != hashMapA[k]:
                return False

        return True


def main():
    s, t = "jill", "b"
    a = Solution()
    answer = a.isAnagram(s, t)
    print(answer)
    assert a.isAnagram("__", "___") == False
    assert a.isAnagram("", "") == True
    assert a.isAnagram("kik", "ik") == False
    assert a.isAnagram("==", "===") == False
    assert a.isAnagram("bob", "obb") == True


if __name__ == '__main__':
    main()
