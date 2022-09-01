# Written by Ted Lawson

import Anagram


class Solution():
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        hashMapA, hashMapB = {}, {}

        for c in range(len(s)):
            hashMapA[s[c]] = 1 + hashMapA.get(s[c], 0)
            hashMapB[t[c]] = 1 + hashMapB.get(t[c], 0)

        for k in hashMapA:
            if hashMapB.get(k, 0) != hashMapA[k]:
                return False

        return True;


def main():
    a = Solution()
    s = 'this'
    t = 'hist'

    print(a.isAnagram(s, t))

    assert a.isAnagram('', '') == True
    assert a.isAnagram('__', '--') == False
    assert a.isAnagram('this', 'that') == False
    assert a.isAnagram('  ', '  ') == True


if __name__ == '__main__': main()
