from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_build(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    if not level_order:
        return None

    iter_order = iter(level_order)
    root_val = next(iter_order)
    if root_val is None:
        return None

    root = TreeNode(root_val)
    queue = deque([root])

    while True:
        try:
            current = queue.popleft()
        except IndexError:
            break

        try:
            left_val = next(iter_order)
            if left_val is not None:
                current.left = TreeNode(left_val)
                queue.append(current.left)
        except StopIteration:
            break

        try:
            right_val = next(iter_order)
            if right_val is not None:
                current.right = TreeNode(right_val)
                queue.append(current.right)
        except StopIteration:
            break

    return root

def tree_print(node: Optional[TreeNode], level: int = 0, label: str = "Root:"):
    if node is not None:
        print(" " * (level * 4) + f"{label} {node.val}")
        tree_print(node.left, level + 1, label="L---")
        tree_print(node.right, level + 1, label="R---")
