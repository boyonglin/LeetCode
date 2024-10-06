from typing import Optional, List
from tree_utils import tree_build, tree_print

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_val = preorder[0]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)

        # preorder ALWAYS has the node first, but you don't know the size of either branch.
        # inorder ALWAYS has the left branch to the left of the node, and right branch right of the node.
        # So now you know the size of each branch.

        l_branch_size = mid  # len(inorder[:mid])
        r_branch_size = len(inorder) - mid - 1  # len(inorder[mid + 1:])

        if l_branch_size:
            root.left = self.buildTree(preorder[1:1 + l_branch_size], inorder[:mid])

        if r_branch_size:
            root.right = self.buildTree(preorder[1 + l_branch_size:], inorder[mid + 1:])

        return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

sol = Solution()
tree_print(sol.buildTree(preorder, inorder))