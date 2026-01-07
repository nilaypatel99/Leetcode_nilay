# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        #preorder or inorder
        MOD=10**9+7
        self.max_product=0

        def total(node):
            if not node:
                return 0
            return node.val + total(node.left) + total(node.right)

        total_sum=total(root)

        def dfs(node):
            if not node:
                return 0

            left=dfs(node.left)
            right=dfs(node.right)

            subtree_sum=node.val+left+right
            
            product=subtree_sum*(total_sum-subtree_sum)

            self.max_product=max(self.max_product,product)

            return subtree_sum

        dfs(root)

        return self.max_product%MOD


            