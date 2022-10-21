# Ted Lawson
from typing import List


def main():
    coins = [8, 12, 2, 10, 5]
    change = 10

    a = Solution().change_calc(coins, change)
    return


class Solution:
    num_coins = 0
    combos = float('inf')

    def change_calc(self, coins: List[int], change: int) -> int:

        if not change:
            print('No solution!')
            return -1

        def dfs(self, coins, change, num_coins):
            if change == 0:
                self.combos = min(self.combos, num_coins)
            if change < 0 or num_coins > self.combos:
                return
            else:
                for coin in coins:
                    dfs(self, coins, change - coin, num_coins + 1)

        dfs(self, coins, change, self.num_coins)
        print(self.combos)

        if self.combos != float('inf'):
            print(f'The min solution is {self.combos} number of coins.')
            return self.combos
        else:
            print('No solution!')
            return -1


if __name__ == "__main__":
    main()
