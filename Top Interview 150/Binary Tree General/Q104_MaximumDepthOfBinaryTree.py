from typing import Optional
from tree_utils import tree_build, tree_print

# definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return 1 + max(left, right)
        else:
            return 0

# Testcase
root = [3, 9, 20, None, None, 15, 7]
tree = tree_build(root)

sol = Solution()
print(sol.maxDepth(tree))