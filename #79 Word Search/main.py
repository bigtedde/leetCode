# Ted Lawson
from typing import List


def main():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
    word = "ABCCED"
    answer = Solution().exist(board, word)
    if answer:
        print("YES - This word DOES exist in the board")
    else:
        print("NO - This word DOES NOT exist in the board")

    return

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return True


if __name__ == "__main__":
    main()
