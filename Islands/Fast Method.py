# Ted Lawson
from typing import List


class Islands:
    def count_islands(self, grid: List[List[str]]) -> int:

        # initialize variables
        num_islands = 0
        rows, columns = len(grid), len(grid[0])

        # Search through the matrix and preform a DFS when you first find land.
        for r in range(0, rows):
            for c in range(0, columns):
                if grid[r][c] == '1':
                    # print(f'New Island, starting at point {r},{c}')
                    num_islands += 1
                    self.dfs(grid, r, c)
        return num_islands

    def dfs(self, grid, r, c):

        # If this point is in bounds and is also part of the island, keep searching for more land
        if (r < 0) or (c < 0) or (r >= len(grid)) or (c >= len(grid[0])) or (grid[r][c] != '1'):
            return
        else:
            grid[r][c] = '#'
            self.dfs(grid, r-1, c)
            self.dfs(grid, r+1, c)
            self.dfs(grid, r, c+1)
            self.dfs(grid, r, c-1)


def main():
    grid = [["1", "1", "1"],
            ["0", "1", "0"],
            ["1", "1", "1"]]

    a = Islands()
    answer = a.count_islands(grid)
    print(f'Number of Islands = {answer}')


if __name__ == '__main__':
    main()
