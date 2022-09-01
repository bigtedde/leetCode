# Ted Lawson
from typing import List


class Solution:
    def buy_sell(self, prices: List[int]) -> int:
        profit, lowest = 0, float('inf')

        if not prices or len(prices) == 1:
            return profit

        for i in range(len(prices)):
            lowest = min(lowest, prices[i])
            n = prices[i] - lowest
            profit = max(profit, n)

        return profit


def main():
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    answer = s.buy_sell(prices)
    print(answer)

    return answer


if __name__ == "__main__":
    main()
