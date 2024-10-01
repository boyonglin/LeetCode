from typing import Optional
from ll_utils import ll_create, ll_print

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        cycle = head

        # get length and move to the last node
        while cycle.next:
            length += 1
            cycle = cycle.next

        k = k % length

        if k == 0:
            return head
        else:
            # create a cycle
            cycle.next = head
            prev = cycle.next

            # init the steps
            k = length - k
            current = cycle.next.next

            for _ in range(k - 1):
                current = current.next
                prev = prev.next

            # break the cycle
            prev.next = None

        return current

# Testcase
head = [1,2]
k = 2

head = ll_create(head)

sol = Solution()
ll_print(sol.rotateRight(head, k))