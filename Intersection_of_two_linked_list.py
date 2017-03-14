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
        ret = self._stack.pop()
        if ret == self._min:
        	if self._stack:
        		self._min = min(self._stack)
        	else:
        		self._min = None
        return ret

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

