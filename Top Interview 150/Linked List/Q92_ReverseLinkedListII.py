# 4o

from ll_utils import createLinkedList, printLinkedList

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        copy = ListNode()
        copy.next = head
        prev = copy

        for _ in range(left - 1):
            prev = prev.next

        # prev = left - 1 node
        # start = left node
        # then = moving node towards right
        start = prev.next
        then = start.next

        # 1 -> 2 -> 3 -> 4
        for _ in range(right - left):
            start.next = then.next  # 2 -> 4
            then.next = prev.next   # 3 -> 2
            prev.next = then        # 1 -> 3
            then = start.next       # then = 4

        return copy.next

# Testcase
head = [1,2,3,4,5]
left = 2
right = 4

head = createLinkedList(head)

sol = Solution()
printLinkedList(sol.reverseBetween(head, left, right))