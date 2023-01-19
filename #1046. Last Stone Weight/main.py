# Ted Lawson on 1/18/23
import heapq
from typing import List


def main():
    stones = [65, 200, 30310, 4100, 5]
    answer = Solution().lastStoneWeight(stones)
    print(f"Remaining weight: {answer}")

    assert Solution().lastStoneWeight([1, 2, 3, 4, 5]) == 1, "Should be 1"
    assert Solution().lastStoneWeight([100, 200, 300, 400, 500]) == 100, "Should be 100"
    assert Solution().lastStoneWeight([65, 200, 30310, 4100, 5]) == 25940, "Should be 25940"

    return

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y = -1*heapq.heappop(maxHeap)
            x = -1*heapq.heappop(maxHeap)
            if x != y:
                newWeight = y-x
                heapq.heappush(maxHeap, -newWeight)

        maxHeap.append(0)
        return -1*maxHeap[0]


if __name__ == "__main__":
    main()
