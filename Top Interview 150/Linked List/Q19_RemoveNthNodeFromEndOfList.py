from typing import Optional

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

def createLinkedList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head

def print_linked_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Testcase
head = [1]
n = 1

head = createLinkedList(head)

sol = Solution()
print_linked_list(sol.removeNthFromEnd(head, n))