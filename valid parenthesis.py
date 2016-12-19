class Solution(object):
    def isValid(self, s):
        left = ['(','{','[']
        right= [')', '}', ']']
        queue = []

        for character in s:
            if character in left:
                queue.append(character)
            if character in right:
                if len(queue) == 0:
                    return False
                if queue.pop()!=left[right.index(character)]:
                    return False
        
        if len(queue) == 0:
            return True
        else:
            return False
