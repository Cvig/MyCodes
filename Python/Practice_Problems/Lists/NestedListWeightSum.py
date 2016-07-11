#Given a nested list of integers, return the sum of all integers in the list weighted by their depth
#Each element is either an integer, or a list whose elements may also be integers or other lists

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.findsum(nestedList, 1)

    def findsum(self, eachlist, depth):
        sum = 0
        for i in range(len(eachlist)):
            if type(eachlist[i]) == int:
                sum += eachlist[i]*depth
            else:
                sum += self.findsum(eachlist[i], depth+1)
        return sum
#Test
'''
s  = Solution()
a = s.depthSum([1,[2,3,4],4])
print a
'''

