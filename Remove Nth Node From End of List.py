# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        border = ListNode(0)
        border.next = head
        a, b = border, border
        
        for i in xrange(n):
            a = a.next

        while a.next:
            a, b = a.next, b.next

        temp = b.next
        b.next = temp.next
        del b

        return border.next


