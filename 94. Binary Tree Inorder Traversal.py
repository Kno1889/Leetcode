# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive O(n)
        result = []

        def IoT(root):
            if not root:
                return
            IoT(root.left)
            result.append(root.val)
            IoT(root.right)
        
        IoT(root)
        return result

        