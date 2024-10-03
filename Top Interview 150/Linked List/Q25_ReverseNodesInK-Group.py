# 4o

from typing import Optional
from ll_utils import ll_create, ll_print

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        reverse = ListNode()
        reverse.next = head

        # init
        prev = reverse
        curr = head

        while curr:
            # check
            tail = curr
            count = 0
            while count < k and tail:
                tail = tail.next
                count += 1

            if count < k:
                return reverse.next

            # reverse
            next_group = tail
            reverse_head = self.reverse_list(curr, k)

            # connect
            prev.next = reverse_head
            curr.next = next_group

            # move
            prev = curr
            curr = next_group

        return reverse.next

    def reverse_list(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        prev = None
        count = 0

        while curr and count < k:
            next_node = curr.next   # store next

            curr.next = prev        # reverse

            prev = curr             # move
            curr = next_node

            count += 1

        return prev



# Testcase
head = [1,2,3,4,5]
k = 2

head = ll_create(head)

sol = Solution()
ll_print(sol.reverseKGroup(head, k))