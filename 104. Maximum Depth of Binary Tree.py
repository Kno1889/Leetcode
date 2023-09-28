# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1) recursive DFS: time & space O(n)
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # -2) iterative DFS: time & space O(n)
        # Queue: add top down, node then left child then right child, then rmeove by layer
        # if not root:
        #     return 0
        
        # level = 0
        # queue = [root]

        # while queue:
        #     for i in range(len(queue)):
                
        #         if root.

        # - iterative BFS

