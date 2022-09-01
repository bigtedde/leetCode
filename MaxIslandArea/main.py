# Ted Lawson
from typing import List


class Solution:
    def max_area_of_island(self, grid: List[List[int]]) -> int:

        # If grid is empty, it has no islands.
        if not grid:
            return 0

        # Initialize variables.
        rows, cols = len(grid), len(grid[0])
        biggest_area = 0

        # Check every element, and preform a dfs if we find a new island.
        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == 1:
                    new_island = self.dfs(grid, r, c)
                    print(f'Island ended at size {new_island}')
                    if new_island > biggest_area:
                        biggest_area = new_island

        return biggest_area

    def dfs(self, grid: List[List[int]], r: int, c: int):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1:
            return 0
        else:
            print(f'New piece of Island at {r},{c}')
            grid[r][c] = 0
            up = self.dfs(grid, r-1, c)
            down = self.dfs(grid, r+1, c)
            right = self.dfs(grid, r, c+1)
            left = self.dfs(grid, r, c-1)
            return 1 + up + down + left + right


def main():
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    s = Solution().max_area_of_island(grid)

    print(f'Max area is {s}')


if __name__ == '__main__':
    main()
