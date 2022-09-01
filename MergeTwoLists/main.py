# Ted Lawson 8/1/22
from typing import Optional
from LinkedList import LinkedList
from Node import Node


class Solution:
    def merge_two_lists(self, list1: LinkedList, list2: LinkedList):
        ll1 = list1.head
        ll2 = list2.head
        answer = dummy = LinkedList()

        return


def main():
    s = Solution()
    ll1, ll2 = LinkedList(), LinkedList()
    list1 = [1, 2, 4, 9, 12, 36, 45]
    list2 = [1, 3, 4, 7]

    for i in list1:
        ll1.add_end(i)
    for j in list2:
        ll2.add_end(j)

    ll1.print()
    print()
    ll2.print()

    # a = s.merge_two_lists(list1, list2)
    # print(a)
    return


if __name__ == '__main__':
    main()
