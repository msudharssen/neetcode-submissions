# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def traverse(root):
            if not root:
                return 0
            
            val1 = traverse(root.left)
            val2 = traverse(root.right)
            return max(val1,val2)+1
        
        return traverse(root)
