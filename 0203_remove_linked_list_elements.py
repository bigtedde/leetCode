# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main():
    linked_list = [0, 1, 2, 3, 4, 5, 6, 1, 2, 3, 7, 7, 8, 9, 0, 0, 1]
    removed_value = 0
    head = createList(linked_list)
    print(f"\nOriginal Linked List: ")
    printElements(head)
    head = removeElements(head, removed_value)
    print(f"\nNew Linked List after removing the {removed_value}'s")
    printElements(head)

def createList(vals: List[int]) -> Optional[ListNode]:
    if not vals:
        return ListNode()
    head = ListNode(vals[0])
    root = head
    for val in vals[1:]:
        head.next = ListNode(val)
        head = head.next

    return root

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next

def printElements(head: Optional[ListNode]) -> None:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


if __name__ == "__main__":
    main()