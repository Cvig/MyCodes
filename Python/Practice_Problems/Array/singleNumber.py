class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(len(nums)):
        #     if nums.count(nums[i]) == 1:
        #         return nums[i]
        temp = sum(list(set(nums)))*2 - sum((nums))
        return temp
