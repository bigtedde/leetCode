# Ted Lawson
from collections import defaultdict
from typing import List


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = groupAnagrams(strs)
    return


def groupAnagrams(strs: List[str]):
    result = defaultdict(list)

    for s in strs:
        count = [0] * 26  # a-z

        for char in s:
            count[ord(char) - ord('a')] += 1

        result[tuple(count)].append(s)

        return result.values


if __name__ == "__main__":
    main()
