# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        
        def traverse(node):
            if not node:
                return
            traverse(node.left)    # Visit left subtree
            result.append(node.val) # Visit root
            traverse(node.right)   # Visit right subtree
            
        traverse(root)
        return result