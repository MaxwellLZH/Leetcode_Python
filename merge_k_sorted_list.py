# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        walker = ListNode(None)
        header = walker

        #add in the first Node
        h = []
        for node in lists:
        	if node:
        		heapq.heappush(h, (node.val, node))

        while h:
        	value, node = heapq.heappop(h)
        	walker.next = node
        	walker = walker.next
        	if node.next:
        		heapq.heappush(h, (node.next.val, node.next))

        return header.next



