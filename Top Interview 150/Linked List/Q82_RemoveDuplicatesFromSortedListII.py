from typing import Optional
from ll_utils import createLinkedList, printLinkedList

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:


# Testcase
head = [1,2,3,3,4,4,5]

head = createLinkedList(head)

sol = Solution()
printLinkedList(sol.deleteDuplicates(head))