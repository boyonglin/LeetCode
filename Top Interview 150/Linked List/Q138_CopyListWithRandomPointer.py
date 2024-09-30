# copilot
from typing import Optional

# definition for a Node
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # interWeaved list: A -> A' -> B -> B' -> C -> C'
        # create a copy of each node and insert it in the original list
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # assign random pointers
        current = head
        while current:
            if current.random:
                # copied current node's random points to copied random node (next)
                current.next.random = current.random.next
            current = current.next.next

        # split the original list and copied list
        current = head
        new_head = head.next
        new_current = new_head
        while current:
            current.next = new_current.next
            current = current.next
            if current:
                new_current.next = current.next
                new_current = new_current.next

        return new_head

# Testcase
head = [[7,None],[13,0],[11,4],[10,2],[1,0]]