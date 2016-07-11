#Given a string S, find the longest palindromic string in S. you may assume that the maximum length of
#S is 1000, and there exists one unique longest palindromic substring

class Solution(object):
    def longestPalindrome(self,s): #aaa, aba, aabbaa
        if len(s) <2: #if its empty or just have one element
            return s
        maxstr =s[0]
        #odd, we get the longest possible palindrome if it exists starting at index i
        for i in range(len(s)):
            str1 = self.getLongestforindex(s,i,i)#for odd
            str2 = self.getLongestforindex(s,i,i+1) #for even
            if len(str1) > len(maxstr):
                maxstr = str1
            if len(str2)> len(maxstr):
                maxstr = str2
        return maxstr


    def getLongestforindex(self, s, start, end):
        while start>=0 and end<len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1:end]
#Test
'''
a ="ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"
s =Solution()
r = s.longestPalindrome(a)
print r
'''