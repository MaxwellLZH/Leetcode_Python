#meidan of two sorted array
#Credit: https://github.com/illuz/leetcode/blob/master/solutions/004.Median_of_Two_Sorted_Arrays/AC_binary_search_logn.py

class Solution:
    def findKthSortedArrays(self, A, B, k):
        if len(A) < len(B):
            A, B = B, A
        if len(B) == 0:
            return A[k - 1]
        if K == 1:
            return min(A[0],B[0])

        #start recursion
        pb = min(k/2, len(B))
        pa = k - pb
        if A[pa - 1] > B[pb -1]:
            return self.findKthSortedArrays(A, B[pb:], k - pb)
        elif A[pa - 1] < B[pb - 1]:
            return self.findKthSortedArrays(A[pa:], B, k - pa)
        else:
            return A[pa - 1]

    # @return a float
    def findMedianSortedArrays(self, A, B):
        if (len(A) + len(B)) % 2 == 1:
            return self.findKthSortedArrays(A, B, (len(A) + len(B)) / 2 + 1)
        else:
            return (self.findKthSortedArrays(A, B, (len(A) + len(B)) / 2) +
                self.findKthSortedArrays(A, B, (len(A) + len(B)) / 2 + 1)) / 2.0


