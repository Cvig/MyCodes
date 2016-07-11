class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds = {} # two dictionaries/mappings because we need to check isomorphism both ways
        dt = {}
        for i in xrange(len(s)):
            if s[i] in  ds.keys() and ds[s[i]] != t[i]: # if character already has a mapping, then check if its same as new one
                return False
            if t[i] in dt.keys() and dt[t[i]] != s[i]: # check in both strings
                return False
            ds[s[i]] = t[i]  # if new character, add it to dictionary
            dt[t[i]] = s[i]
        return True

# Isomorphism needs to be checked both ways. E.g. "aa" and "ab" should return false even if ab to aa returns True
# There could be very long strings with non-alpha characters as well so time-complexity is important.
# This one is of O(n)
# sol = Solution()
# sol.isIsomorphic('acd','bjd')

