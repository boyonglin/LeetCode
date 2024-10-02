from typing import Optional
from ll_utils import ll_create, ll_print

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater = ListNode()
        less = ListNode()

        cur_g = greater
        cur_l = less

        while head:
            if head.val >= x:
                cur_g.next = ListNode(head.val)
                cur_g = cur_g.next
            else:
                cur_l.next = ListNode(head.val)
                cur_l = cur_l.next

            head = head.next

        cur_l.next = greater.next

        return less.next

# Testcase
head = [2,1]
x = 2

head = ll_create(head)

sol = Solution()
ll_print(sol.partition(head, x))