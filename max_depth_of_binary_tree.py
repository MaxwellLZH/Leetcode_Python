# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def sortedArrayToBST(self, nums):

		root = TreeNode(None)
		self.helper(root, nums)
		return root


   	def helper(self, node, nums):
	   	if nums:	
	   		left, right = 0, len(nums) -1
	   		mid = (left + right) / 2
	   		node.val = nums[mid]
	   		node.left, node.right = TreeNode(None), TreeNode(None)
	   		self.helper(node.left, nums[left:mid])
	   		self.helper(node.right, nums[mid:right])

