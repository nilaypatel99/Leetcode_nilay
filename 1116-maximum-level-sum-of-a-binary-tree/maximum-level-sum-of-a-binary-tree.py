# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        lvl_sum=defaultdict(int)

        def dfs(node,lvl):
            if not node:
                return 
            lvl_sum[lvl]+=node.val

            dfs(node.left,lvl+1)
            dfs(node.right,lvl+1)

        dfs(root,1)
        max_sum=float('-inf')
        res_lvl=0

        for lvl,total in lvl_sum.items():
            if total>max_sum:
                max_sum=total
                res_lvl=lvl

        return res_lvl
