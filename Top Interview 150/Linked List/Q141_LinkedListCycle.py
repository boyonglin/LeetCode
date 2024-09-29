from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow-fast pointers
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

def createLinkedList(arr, pos = -1):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    cycle_node = None

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
        if i == pos:
            cycle_node = current

    if cycle_node:
        current.next = cycle_node

    return head

# Testcase
head = [3,2,0,-4]
pos = 1

head = createLinkedList(head, pos)

sol = Solution()
print(sol.hasCycle(head))