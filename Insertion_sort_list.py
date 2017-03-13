# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = dummy = ListNode(0)
        while head:
        	if head.val < cur.val:
        		cur = dummy
        	while cur.next and cur.next.val < head.val:
        		cur = cur.next
        	cur.next, cur.next.next, head = head, cur.next, head.next
        return dummy.next


    
a = ListNode(3)
b = ListNode(4)
c = ListNode(5)
a.next = b
b.next = c
c.next = None

s = Solution()
s.insertionSortList(a)