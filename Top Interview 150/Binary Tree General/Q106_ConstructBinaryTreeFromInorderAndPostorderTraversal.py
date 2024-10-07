from typing import Optional, List
from tree_utils import tree_build, tree_print

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root_value = postorder[-1]
        root = TreeNode(root_value)
        mid = inorder.index(root_value)

        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])

        return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

sol = Solution()
tree_print(sol.buildTree(inorder, postorder))