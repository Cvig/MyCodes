#Rotate an array by k steps

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     a = nums.pop(len(nums)-1)# remove last element from the list, be careful on index, it should be len(nums) -1 and not len(nums)
        #     nums = [a] + nums   #add the element at the front, you can't use append here as it only adds an element at the end
        #a = nums[len(nums)-k:]
        #print a # a is [2]
        #b = nums[0:len(nums)-k] #it shouldn't be len(nums) -k-1. It should be len(nums) - k only.
        a = nums[len(nums)-k:]

        b = nums[:len(nums)-k]
        # print a
        # print b
        c =  a + b
        nums[:]  = c  # why do we need [:] and why nums won't work??????????????????????????? It works on my IDE though :P
        return  nums

s = Solution()
a = [1,2]
k = 1
r = s.rotate(a,k)
print r
b = [1,2]
print b[:]