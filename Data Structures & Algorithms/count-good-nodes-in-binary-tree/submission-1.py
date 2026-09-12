# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.total = 0
        def dfs(curr, maxVal):
            if not curr:
                return None

            if curr.val >= maxVal:
                self.total+=1
            
            currMax = max(maxVal, curr.val)
            dfs(curr.left, currMax)
            dfs(curr.right, currMax)
            return curr
        
        dfs(root, root.val)
        return self.total
            