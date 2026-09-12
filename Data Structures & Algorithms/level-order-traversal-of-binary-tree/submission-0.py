# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        allNodes = deque()
        allNodes.append(root)

        while allNodes:
            size = len(allNodes)
            level = []
            for i in range(size):
                curr = allNodes.popleft()
                level.append(curr.val)
                if curr.left:
                    allNodes.append(curr.left)
                if curr.right:
                    allNodes.append(curr.right)
            res.append(level)
        return res