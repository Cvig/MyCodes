class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        temp = sum(list(set(nums)))*2 - sum((nums))
        return temp
