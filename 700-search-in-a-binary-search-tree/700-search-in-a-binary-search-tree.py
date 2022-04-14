# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def traversal(src):
            if src == None:
                return src
            if src.val==val:
                return src
            elif src.val>val:
                return traversal(src.left)
            else:
                return traversal(src.right)
            
        return traversal(root)