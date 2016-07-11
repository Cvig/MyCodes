# Given an input string, reverse the string word by word
#just add space at the end of the given string, find revstr and at the end, just remove space at the end
class Solution(object):
    def reverseWords(self,s):
        revstr = "" #This is the output string
        word = ""  # This will contain each word to be added at the front of revstr to complete it
        s = s + ' '
        for each in s: #We will check each string
            if each != ' ':
                word = word+each
            if each == ' ' and len(word)!=0:  #we have reached to the end of the word
                revstr = word +' ' +revstr  #add word to the front, mind that we have extra space at the end
                word =''#reset the word
       
        revstr = revstr[:-1]
        return revstr
#Test
'''
s = Solution()
r = s.reverseWords("hello miss and hello again")
print r
'''




