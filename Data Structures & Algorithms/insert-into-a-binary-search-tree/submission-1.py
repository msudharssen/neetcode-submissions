# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        curr = root

        def dfs(curr):
            if not curr:
                toAdd = TreeNode(val, None, None)
                return toAdd
            if curr.val < val:
                curr.right = dfs(curr.right)
            if curr.val > val:
                curr.left = dfs(curr.left)
            return curr
        
        ans = dfs(root)
        return ans

        

