# Ted Lawson
import heapq
from typing import List


def main():
    return


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        print(f"INIT: nums: {self.minHeap}")
        print(f"INIT: k: {self.k}")

        heapq.heapify(self.minHeap)
        print("INIT: Created heap is : ", (list(self.minHeap)))

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        print("INIT: Heap after initial poping is : ", (list(self.minHeap)))

    def add(self, val: int) -> int:
        if len(self.minHeap) == self.k:
            popped = heapq.heappushpop(self.minHeap, val)
            print(f"ADD: minheap = length {self.k}, pushed in {val} popped out {popped}")
        else:
            heapq.heappush(self.minHeap, val)
            print(f"ADD: minheap size {len(self.minHeap)}, k = {self.k}, pushed in {val}")

        return self.minHeap[0]


if __name__ == "__main__":
    main()
