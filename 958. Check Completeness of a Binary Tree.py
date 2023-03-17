# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [root]
        is_last = False

        while queue:
            node = queue.pop(0)

            if (
                not node.left and node.right
            ):  # if no left child, but there is a right child, tree is incomplete
                return False

            if is_last and (node.left or node.right):
                return False

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            if not node.left or not node.right:
                is_last = True

        return True
