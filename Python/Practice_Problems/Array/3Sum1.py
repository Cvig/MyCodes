class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #brute force way, not efficient
        mylist = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        a = [nums[i],nums[j],nums[k]]
                        a = sorted(a)
                        a = tuple(a)
                        if a in mylist:  
                            continue
                        else:
                            mylist.append(a)
        return mylist 

#Test
'''
a = [-6,-8,-9,4,-14,6,-10,7,12,13,4,9,7,14,-12,7,0,14,-1,-3,2,2,-3,11,-6,-10,-13,-13,1,-9,2,2,-2,8,-9,0,-9,-12,14,10,8,3,4,0,-6,7,14,9,6,-2,13,-15,8,-5,3,-13,-8,5,-11,0,11,6,-13,-14,-9,-15,-7,-11,10,-7,14,4,3,3,11,13,-13,11,-1,0,-6,-10,0,9,0,10,11,0,0,-14,-15,-12,-1,10,12,-2,2,-10,2,-2,-10,2,-13,1,12,5,-1,-15,1,5,-8,3,10,8]
s = Solution()
r = s.threeSum(a)
print len(r)
'''
