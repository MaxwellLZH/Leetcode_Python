class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total, count = 0, 0
        for i in range(len(nums)):
        	if nums[i] > 0:
        		count += 1
        		total += i
        	
        if total == (count + 1) * count /2:
        	return count + 1
        else:
			return  count + 1 +  (count + 1) * count /2 - total




class Solution2:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        n = len(A)
        i = 0
        if n==0: return 1
        while i<n:
            while A[i]!=i+1 and A[i]<=n and A[i]>0 and A[i]!=A[A[i]-1]: 
                t = A[i]
                A[i] = A[A[i]-1] 
                A[t-1] = t
            i = i+1
        for i in xrange(n):
            if A[i]!=i+1: return i+1
        return n+1

s = Solution2()
t = s.firstMissingPositive([-1, 0, 1,1,2,4, 5, 6])
print t

