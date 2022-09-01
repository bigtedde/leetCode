# Ted Lawson 8/7/22
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, ending_color: int) -> List[List[int]]:

        starting_color = image[sr][sc]

        if starting_color == ending_color:
            return image

        return self.dfs(image, sr, sc, starting_color, ending_color)

    def dfs(self, image: List[List[int]], row: int, col: int, starting_color: int, ending_color: int):

        if row == len(image) or row < 0 or col == len(image[0]) or col < 0 or image[row][col] != starting_color:
            return
        else:
            image[row][col] = ending_color
            # scan up, down, left, right for continued fill
            self.dfs(image, row - 1, col, starting_color, ending_color)
            self.dfs(image, row + 1, col, starting_color, ending_color)
            self.dfs(image, row, col - 1, starting_color, ending_color)
            self.dfs(image, row, col + 1, starting_color, ending_color)

        return image


def main():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2

    answer = Solution().floodFill(image, sr, sc, color)
    print(answer)
    return answer


if __name__ == '__main__':
    main()
