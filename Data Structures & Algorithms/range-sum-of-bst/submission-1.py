# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0

        def traverse(curr):
            if not curr:
                return
            
            if curr.val > low:
                traverse(curr.left)
            if curr.val < high:
                traverse(curr.right)
            if low <= curr.val <= high:
                self.res+=curr.val
            return curr
        
        traverse(root)
        return self.res
