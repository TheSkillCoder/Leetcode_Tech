# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        smm=0
        def fun(root):
            nonlocal smm
            if root == None:
                return
            smm+=root.val
            fun(root.left)
            fun(root.right)
        fun(root)
        
        def ans_map(root):
            nonlocal smm
            if root == None:
                return
            ans_map(root.left)
            temp=root.val
            root.val=smm
            smm-=temp
            ans_map(root.right)
        ans_map(root)
        
        return root