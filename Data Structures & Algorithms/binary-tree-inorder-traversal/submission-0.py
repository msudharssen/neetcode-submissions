# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(root, result):
            if not root:
                return None
            
            traverse(root.left, result)
            result.append(root.val)
            traverse(root.right, result)
            return 
        
        traverse(root, res)
        return res