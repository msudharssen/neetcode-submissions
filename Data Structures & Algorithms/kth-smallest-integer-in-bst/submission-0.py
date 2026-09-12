# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []


        def traverse(root, ref):
            if not root:
                return None
            
            traverse(root.left, ref)
            ref.append(root.val)
            traverse(root.right, ref)
            return
        
        traverse(root, res)
        return res[k-1]