#Zigzag words


from collections import defaultdict

class Solution(object):
    def convert(self, s, numRows):
        byrow =  defaultdict(list)
        for index, character in enumerate(s):
            byrow[index % numRows].append(character)
        output_list = [item for sublist in byrow.values() for item in sublist]
        print byrow
        print ''.join(output_list)

        

