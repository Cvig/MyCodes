#Given a string S, find the longest palindromic string in S. you may assume that the maximum length of
#S is 1000, and there exists one unique longest palindromic substring

class Solution(object):
    def longestPalindrome(self,s):
        if len(s) < 2:
            return s

        maxstr = s[0] #this will have longest substring
        for i in xrange(0,len(s)): #want to iterate each character in s
            for j in xrange(i+1, len(s)):
                sub = s[i:j]
                if self.isPalindrom(sub):
                    if len(sub) > len(maxstr):
                        maxstr = sub
        return maxstr

    def isPalindrom(self,s):
        s =s.lower() #because caps and lowers will return false while comparing them but they should be same
        for i in xrange(0,len(s)):
            if s[i] != s[len(s) -i-1]:
                return False
        return True

#Test
# a ="ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"
# s =Solution()
# r = s.longestPalindrome(a)
# print r