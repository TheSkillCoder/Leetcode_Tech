# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first=None
        middle=None
        last=None
        prev=TreeNode(float('-inf'))

        def inorder(root):
            nonlocal first,middle,last,prev
            if (root==None):
                return

            inorder(root.left)
            if (prev!=None and (root.val<prev.val)):
                if (first == None):
                    first=prev
                    middle=root
                else:
                    last=root

            prev=root
            inorder(root.right)

        inorder(root)
        if (first!=None and last!=None):
            temp=first.val
            first.val=last.val
            last.val=temp

        else:
            if (first!=None and middle!=None):
                temp=first.val
                first.val=middle.val
                middle.val=temp