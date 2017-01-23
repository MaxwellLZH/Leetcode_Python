# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
        	return []

        queue = [(root, 0)]
        ret, res = [], []
        while queue:
  			cur = queue.pop(0)
  			node, level = cur[0], cur[1]
  			ret.append((node.val, level))
  			if node.left:
  				queue.append((node.left, level + 1))
  			if node.right:
  				queue.append((node.right, level + 1))
        depth = ret[-1][1]
        for i in range(depth + 1):
        	res.append([value[0] for value in ret if value[1] == i])
        return res