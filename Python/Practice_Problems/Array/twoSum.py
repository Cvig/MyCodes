class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # There are exactly two elements in the sum i.e. only one solution
        for i in xrange(0, len(nums)):
            first = nums[i]   #let the element in consideration as first element
            second = target - first   # then the second element should be the difference between target and the first element
            if second in nums[i+1:]:  # You need to exclude first element
                return [i, nums[i+1:].index(second) +i+1]  # after u exclude, u need to get index correctly by adding i+1

        return [-1]
'''
Cases:
[-3,4,3,90], 0  # if u check for 0 separately, this would have caused the problem
[0,4,3,0], 0    # if you don't do indexing properly, u might get [0,0] or [0,2] instead of [0,3]
[3,4,4,3], 6    # u might get [0,0] indices for target 6 if u dont exclude the first element in consideration
'''
# s = Solution()
# res = s.twoSum([3,4,4],6)

