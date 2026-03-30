# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
binary tree means 2 children per node max. 
**Locally optimal decisions 

check heights of each node children. 

Base case: No children = height is 1 
recur when node has children: each time we check heights and then its sub children

'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        heights = {} # node:height
        def height_helper(node):
            if not node:
                return 0
            
            heights[node] = 1 + max(height_helper(node.left), height_helper(node.right))
            return heights[node]
        height_helper(root)

        def balance_helper(node):
            if not node:
                return True
            if node.left in heights:
                left = heights[node.left]
            else:
                left = 0
            
            if node.right in heights:
                right = heights[node.right]
            else:
                right = 0

            return (abs(left - right) <= 1) and  balance_helper(node.left) and balance_helper(node.right)
        return balance_helper(root)
