# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def traverseTree(node, elements):
            if not node:
                return
            
            traverseTree(node.left, elements)
            elements.append(node.val)
            traverseTree(node.right, elements)


        elements1 = []
        elements2 = []
        
        traverseTree(root1, elements1)
        traverseTree(root2, elements2)
        
        # return sorted(elements) # O(nlogn) => make 2 lists, merge them using the 2-pointer method

        elements = []
        i, j = 0, 0

        while (i < len(elements1)) and (j < len(elements2)):
            if elements1[i] < elements2[j]:
                elements.append(elements1[i])
                i += 1
            else:
                elements.append(elements2[j])
                j += 1
        
        return elements + elements1[i:] + elements2[j:]
