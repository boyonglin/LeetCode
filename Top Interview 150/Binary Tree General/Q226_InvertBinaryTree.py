from typing import Optional
from tree_utils import tree_build, tree_print

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Testcase
root = [4,2,7,1,3,6,9]
tree = tree_build(root)
tree_print(tree)

sol = Solution()
tree_print(sol.invertTree(tree))