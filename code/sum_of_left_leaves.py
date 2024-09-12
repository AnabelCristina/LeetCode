# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def is_leaf(node) -> bool:
            return node.left == None and node.right == None       

        if(root==None):
            return 0
        
        left_sum = 0
        
        if (root.left != None):
            if is_leaf(root.left):
                left_sum += root.left.val
            else:
                left_sum += self.sumOfLeftLeaves(root.left)
        
        left_sum += self.sumOfLeftLeaves(root.right)


        return left_sum