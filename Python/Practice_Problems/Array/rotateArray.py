#Rotate an array by k steps

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        b = nums[:len(nums)-k]
        c =  a + b
        nums[:]  = c  
        return  nums
#Test
'''
s = Solution()
a = [1,2]
k = 1
r = s.rotate(a,k)
print r
b = [1,2]
print b[:]
'''