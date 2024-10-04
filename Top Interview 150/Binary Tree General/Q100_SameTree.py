from typing import Optional
from tree_utils import tree_build, tree_print

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True

        # if not p or not q:
        #     return False

        # if p.val != q.val:
        #     return False

        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q  # true if both are None or same object in memory

# Testcase
p = [1,2,3]
q = [1,2,3]
p = tree_build(p)
q = tree_build(q)

sol = Solution()
print(sol.isSameTree(p, q))