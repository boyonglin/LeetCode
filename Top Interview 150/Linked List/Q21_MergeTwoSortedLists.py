from typing import Optional
from ll_utils import createLinkedList, printLinkedList

# definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        current = res

        while list1 or list2:
            if list1 is None:
                current.next = list2
                break

            if list2 is None:
                current.next = list1
                break

            a = list1.val
            b = list2.val

            if a > b:
                current.next = ListNode(b)
                list2 = list2.next
            else:
                current.next = ListNode(a)
                list1 = list1.next

            current = current.next

        return res.next

# Testcase
list1 = [1,2,4]
list2 = [1,3,4]

list1 = createLinkedList(list1)
list2 = createLinkedList(list2)

sol = Solution()
printLinkedList(sol.mergeTwoLists(list1, list2))