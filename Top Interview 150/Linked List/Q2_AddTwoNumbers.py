from typing import Optional
from ll_utils import ll_create, ll_print

# definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = ListNode()
        current = sum
        carry = 0

        while l1 or l2:
            if l1 is None:
                l1 = ListNode()
            if l2 is None:
                l2 = ListNode()

            temp = l1.val + l2.val + carry

            if temp // 10 > 0:
                carry = temp // 10
                temp = temp % 10
            else:
                carry = 0

            l1 = l1.next
            l2 = l2.next
            current.next = ListNode(temp)
            current = current.next

        if carry > 0:
            current.next = ListNode(carry)

        return sum.next

# Testcase
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

l1 = ll_create(l1)
l2 = ll_create(l2)

sol = Solution()
ll_print(sol.addTwoNumbers(l1, l2))