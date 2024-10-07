from tree_utils import tree_build, tree_print

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return

        queue = [root]

        while queue:
            current_level_size = len(queue)

            # Connect nodes in the same level
            for i in range(current_level_size):
                node = queue.pop(0)

                if i < current_level_size - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root

root = [1,2,3,4,5,None,7]
root = tree_build(root)

sol = Solution()
print(sol.connect(root))