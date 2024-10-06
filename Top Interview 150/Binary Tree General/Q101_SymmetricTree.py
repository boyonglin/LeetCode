from typing import Optional
from tree_utils import tree_build, tree_print

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l = root.left
        r = root.right

        def isMirror(l, r):
            if not l and not r:
                return True

            if not l or not r:
                return False

            if l.val != r.val:
                return False

            # check -> in left tree and <- in right tree
            return isMirror(l.left, r.right) and isMirror(l.right, r.left)

        return isMirror(l, r)

# Testcase
root = [1,2,2,3,4,4,3]
root = tree_build(root)

sol = Solution()
print(sol.isSymmetric(root))