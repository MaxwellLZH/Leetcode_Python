# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self._helper(root, ret)
        return ret
    

    def _helper(self, root, ret):
    	if root:
    		ret.append(root.val)
    		self._helper(root.left, ret)
    		self._helper(root.right, ret)