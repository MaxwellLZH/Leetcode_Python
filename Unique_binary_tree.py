# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
    	p_generator  = inorder_travel(p)
    	q_generator  = inorder_travel(q)
    	while 1:
	    	try:
	    		if p_generator.next() == q_generator.next():
	    			pass
	    		except StopIteration:
	    			return True
	    		else:
	    			return False
	    

   	def inorder_travel(self, p):
   		if p.left:
   			yield self.inorder_travel(p.left)
   		yield p.val
   		if p.right:
   			yield self.inorder_travel(p.right)

