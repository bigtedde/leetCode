from typing import List


def main():
    s = Solution()
    answer = s.generate(5)
    for row in answer:
        print(row)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        prev_row, cur_row, answer = [1], [], [[1]]
        for row in range(1, numRows):
            for index in range(len(prev_row) + 1):
                if index == 0 or index == len(prev_row):
                    cur_row.append(1)
                else:
                    cur_row.append(prev_row[index] + prev_row[index - 1])
            answer.append(cur_row)
            prev_row, cur_row = cur_row, []
        return answer


if __name__ == "__main__":
    main()