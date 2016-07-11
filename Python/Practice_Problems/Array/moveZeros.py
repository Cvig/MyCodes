class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == None:
            return nums
        count = nums.count(0)
        for i in range(0,count):
            nums.remove(0)
            nums.append(0)
        