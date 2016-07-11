'''
A program to reverse and print given string.

Cases:
1. ''
2. '\unicode'
3. 'My name is Chetna'  #antehc si eman yM
4. cat #tac
'''

class Solution(object):
    def reverseString(self, s):
		"""
        :type s: str
        :rtype: str
        """
        print s[::-1]

class Solution2(object):
    def reverseString2(self, s):
        if len(s) == 0:
            return s
        length = len(s) #3
        revStr = ''
        try:
            for i in range(length): #i = 0, 1, 2
                revStr = s[i] + revStr # when i =0 , revStr = c, ac, tac
        except:
            print("error")

        print revStr
#Test
'''
s = Solution2()
s.reverseString2("cat is dog")
'''