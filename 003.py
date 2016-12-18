#longest substring with no repetition

class Solution(object):
    def lengthOfLongestSubstring(self, s):
    	current_substring, max_substring = '', ''
    	current_length, max_length = 0, 0
    	for character in s:
    		if character not in current_substring:
    			current_length += 1
    			current_substring += character
    		else:
    			if current_length > max_length:
    				max_length, max_substring= current_length, current_substring
    			start_point = current_substring.find(character)
    			current_substring = current_substring[start_point+1:] + character
    			current_length = len(current_substring)

    	#compare current and max length when for loop ends
    	return current_length if current_length > max_length else max_length

#s = Solution()
#s.lengthOfLongestSubstring('teauhsdo')






        
