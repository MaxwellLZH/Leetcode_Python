#Palindrome integer

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            num = str(abs(x)).strip()
            rev_num = num[::-1]
            return True if num == rev_num else False
