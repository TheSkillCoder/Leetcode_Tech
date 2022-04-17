# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def rec(root):
            if root:
                rec(root.left)
                root.left=None
                self.curr.right=root
                self.curr=root
                rec(root.right)
                
        ans=self.curr=TreeNode(None)
        rec(root)
        return ans.right