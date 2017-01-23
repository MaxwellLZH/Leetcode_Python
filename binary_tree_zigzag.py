# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
    	ret, level, depth = [], [root], 1
    	while root and level:
    		if depth % 2 == 1:
    			ret.append([node.val for node in level])
    		else:
    			level.reverse()
    			ret.append([node.val for node in level])
    			level.reverse()
    		children_pairs = [(node.left, node.right) for node in level]
    		level = [node for pair in children_pairs for node in pair if node]
    		depth += 1
    	return ret