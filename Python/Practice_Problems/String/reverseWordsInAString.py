# Given an input string, reverse the string word by word
# class Solution(object):
#     def reverseWords(self,s):
#         revstr = "" #This is the output string
#         word = ""  # This will contain each word to be added at the front of revstr to complete it
#         for each in s: #We will check each string
#             if each!=' ':
#                 word = word+each
#             if each == ' ' and len(word)!=0:  #we have reached  the end of the word
#                 revstr = word +' ' +revstr  #add word to the front, mind that we have extra space at the end
#                 word =''#reset the word
#         #mind that we can have last word as non-empty but still havent added to the revstr as we might not encounter space at the end
#         # and the conditiont to add word to the revstr is space at the end of the word
#         if len(word)!=0: ####This is important to note that last word needs to be handled carefully, "1 "
#             ##we need to check length because otherwise we'll unnecessary add space at the end
#             revstr = word+' '+revstr
#         revstr = revstr[:-1]
#         return revstr

#just add space at the end of the given string, find revstr and at the end, just remove space
class Solution(object):
    def reverseWords(self,s):
        revstr = "" #This is the output string
        word = ""  # This will contain each word to be added at the front of revstr to complete it
        s = s + ' '
        for each in s: #We will check each string
            if each != ' ':
                word = word+each
            if each == ' ' and len(word)!=0:  #we have reached  the end of the word
                revstr = word +' ' +revstr  #add word to the front, mind that we have extra space at the end
                word =''#reset the word
        #mind that we can have last word as non-empty but still havent added to the revstr as we might not encounter space at the end
        # and the conditiont to add word to the revstr is space at the end of the word
        #if len(word)!=0: ####This is important to note that last word needs to be handled carefully, "1 "
            ##we need to check length because otherwise we'll unnecessary add space at the end
        #revstr = word+' '+revstr
        revstr = revstr[:-1]
        return revstr


s = Solution()
r = s.reverseWords("hello miss and hello again")
print r

# This solution won't work for all cases like " ", " a ", etc.
# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         mylist = s.split(" ")
#         str = ''
#         for i in range(len(mylist)-1,-1,-1): #-1 because u want to include 0 also
#             str += mylist[i]+" "
#
#         return str




