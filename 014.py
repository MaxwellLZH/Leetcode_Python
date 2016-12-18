#longest common prefix

class Solution(object):
    def pairwisePrefix(self, A, B):
        ret = ''
        A, B = A.strip(), B.strip()
        l = min(len(A), len(B))
        for i in range(l):
            if A[i] == B[i]:
                ret += A[i]
        return ret

    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            prefix = self.pairwisePrefix(strs[0], strs[1])
            if prefix == '':
                return ''
            for i in range(len(strs)):
                prefix = self.pairwisePrefix(prefix, strs[i])
                if prefix == '':
                    return ''

        return prefix
