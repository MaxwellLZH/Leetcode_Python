class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min = None
        self._stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)
        if self._min is None:
        	self._min = x
        else:
        	self._min = min(x, self._min)

    def pop(self):
        """
        :rtype: void
        """
        return self._stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._min


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print obj.getMin()
print obj.pop()
print obj.top()
print obj.getMin()