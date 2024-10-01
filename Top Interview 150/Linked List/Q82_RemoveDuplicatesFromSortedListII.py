from typing import Optional
from ll_utils import ll_create, ll_print

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return head

# Testcase
head = [1,2,3,3,4,4,5]

head = ll_create(head)

sol = Solution()
ll_print(sol.deleteDuplicates(head))