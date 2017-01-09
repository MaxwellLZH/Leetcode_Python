class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        try:
            while True:
                pre, cur, nxt = cur, cur.next, cur.next.next
                # change the position of cur and nxt
                pre.next, cur.next, nxt.next = nxt, nxt.next, cur
                # now cur is in the third place
        except:
            return dummy.next