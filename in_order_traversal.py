# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
     	self.ret = []
     	self._inorder(root)
     	return self.ret


    def _inorder(self, node):
	    if node:	
	    	if node.left:
	    		self._inorder(node.left)
	    	self.ret.append(node.val)
	    	if node.right:
	    		self._inorder(node.right)
