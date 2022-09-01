# Ted Lawson
from typing import List


class Islands:
    def count_islands(self, grid: List[List[str]]) -> int:

        # initialize variables
        num_islands = 0
        visited, queued = [], []
        rows, columns = len(grid), len(grid[0])

        for r in range(0, rows):
            for c in range(0, columns):
                if grid[r][c] == '1' and (r, c) not in visited:
                    visited.append((r, c))
                    queued.append((r, c))
                    # print(f'New Island, starting at point {r},{c}')
                    num_islands += 1

                    # while there are still items queued, pop from queue and preform BFS
                    while queued:
                        x, y = queued.pop(0)

                        # Check left for a 1
                        if x - 1 >= 0 and grid[x - 1][y] == '1' and (x - 1, y) not in visited:
                            # print(f'Queued: {x-1},{y}')
                            visited.append((x - 1, y))
                            queued.append((x - 1, y))

                        # Check right for a 1
                        if x + 1 < rows and grid[x + 1][y] == '1' and (x + 1, y) not in visited:
                            # print(f'Queued: {x+1},{y}')
                            visited.append((x + 1, y))
                            queued.append((x + 1, y))

                        # Check down for a 1
                        if y - 1 >= 0 and grid[x][y - 1] == '1' and (x, y - 1) not in visited:
                            # print(f'Queued: {x},{y-1}')
                            visited.append((x, y-1))
                            queued.append((x, y-1))

                        # Check up for a 1
                        if y + 1 < columns and grid[x][y + 1] == '1' and (x, y + 1) not in visited:
                            # print(f'Queued: {x},{y+1}')
                            visited.append((x, y + 1))
                            queued.append((x, y + 1))
        return num_islands


def main():
    grid = [["1", "1", "1"],
            ["0", "1", "0"],
            ["1", "1", "1"]]

    a = Islands()
    answer = a.count_islands(grid)
    print(f'Number of Islands = {answer}')


if __name__ == '__main__':
    main()
