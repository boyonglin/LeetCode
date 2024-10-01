class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def printLinkedList(node):
    values = []

    while node:
        values.append(str(node.val))
        node = node.next

    print(" -> ".join(values))