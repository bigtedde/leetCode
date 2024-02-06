# Ted Lawson
from typing import List


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
    return


class Solution:
    def groupAnagrams(self, strs: List[str]):

        result = {}
        final_result_list_of_lists = []

        for word in strs:
            letters = {}
            for letter in word:
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
            result[word] = letters

            while result:
                value = result[0]
                list_final = []
                for k, v in result:
                    if v == value:
                        list_final.append(k)
                        result.pop(k)
                final_result_list_of_lists.append(list_final)





                result[word].value.append = [letter]

        return result


if __name__ == "__main__":
    main()
