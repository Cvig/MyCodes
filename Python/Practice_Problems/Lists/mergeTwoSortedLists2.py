#This is easy pythonic way to do the problem

class Solution(object):
    def mergeTwoLists(self,l1,l2):
        return sorted(l1+l2)

# sol = Solution()
# li = sol.mergeTwoLists([2,3,8],[-3,5,8])
# print li