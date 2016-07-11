class Solution(object):
    def mergeTwoLists(self, l1,l2):
        l3= []
        i =j =0
        while True:
            if i == len(l1):
                return l3 + l2[j:]
            if j == len(l2):
                return l3 + l1[i:]

            if l1[i] <= l2[j]:
                l3.append(l1[i])
                i = i+1
            else:
                l3.append(l2[j])
                j = j+1
#Test
# s = Solution()
# l3 = s.mergeTwoLists([1,2,3,4,9],[5,6,7,8])
# print l3