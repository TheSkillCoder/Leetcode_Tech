class BSTIterator:
    
	# finds the leftmost descendant of currentNode
    def moveLeftest(self):
        while self.currentNode.left:
            self.nodeStack.append(self.currentNode)
            self.currentNode = self.currentNode.left

    def __init__(self, root: Optional[TreeNode]):
        self.nodeStack = []
        self.currentNode = root
		# the first node in inorder traversal is the leftmost descendant of root
        self.moveLeftest()
		# we move one position to the left to phantom node
        self.nodeStack.append(self.currentNode)
        self.currentNode = TreeNode(-1)

    def next(self) -> int:
	    # if currentNode has a right child, we move towards it, and 
		# then go to its leftmost descendant
        if self.currentNode.right:
            self.currentNode = self.currentNode.right
            self.moveLeftest()
		# if currentNode does not have a right child, the next node in
		# inorder traversal is the back node of nodeStack
        else:
            self.currentNode = self.nodeStack.pop()
        return self.currentNode.val

    def hasNext(self) -> bool:
	    # there is a node to move to if currentNode has a right child
		# or if nodeStack is not empty
        if self.currentNode.right or self.nodeStack:
            return True
        return False