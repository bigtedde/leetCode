# Ted Lawson 8/7/22
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = dict()
        t_dict = dict()

        # Create dicts of all chars in s and t strings, where [key] = chars, [value] = number of occurrences
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        print(s_dict)

        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1
        print(t_dict)

        return s_dict == t_dict


def main():
    s = "this string"
    t = "string this"

    answer = Solution().is_anagram(s, t)
    print(answer)
    return answer


if __name__ == '__main__':
    main()
