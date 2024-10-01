from typing import Optional
from ll_utils import createLinkedList, printLinkedList

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        remove = ListNode()
        remove.next = head
        delay = remove
        current = remove

        for _ in range(n + 1):
            current = current.next

        while current:
            delay = delay.next
            current = current.next

        delay.next = delay.next.next

        return remove.next

# Testcase
head = [1,2,3,4,5]
n = 2

head = createLinkedList(head)

sol = Solution()
printLinkedList(sol.removeNthFromEnd(head, n))