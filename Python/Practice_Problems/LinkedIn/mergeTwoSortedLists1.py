class Solution(object):
    def mergeTwoLists(self,l1,l2):
        l3 = []
        i=0
        j=0
        while i!=len(l1) and j!=len(l2):
            if l1[i] < l2[j]:
                l3.append(l1[i])
                i = i+1
            else:
                l3.append(l2[j])
                j = j+1
        if i == len(l1):
            return l3+l2[j:]
        else:
            return l3+l1[i:]
# s = Solution()
# l3 = s.mergeTwoLists([],[])
# print l3

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
# This one I just tried but its not working
# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         l3 = []
#         # what if one is empty and the other one is not?
#         if len(l1) == 0 and len(l2) > 0:
#             return l2
#         elif len(l2) == 0 and len(l1) >0:
#             return l1
#         elif len(l2) > len(l1):
#             for i in xrange(0,len(l1)):
#                 j = i
#                 while l1[i] >= l2[j] and len(l2) >= j:
#                     l3.append(l2[j+i])
#                     j += 1
#                 l3.append(l1[i])
#         elif len(l2) <= len(l1): #runtime sybtax error, None type
#             for i in xrange(0,len(l2)): #i=0,1,2,3
#                 j = i  #j=0,1,2,3
#                 print i,j, l2[i], l1[j], len(l1)
#                 while j+i < len(l1) and l2[i] > l1[j] : # where u put condition in while statement matters, why ???
#                     l3.append(l1[j+i])
#                     j += 1
#                 l3.append(l2[i])
#
#         return l3

# s = Solution()
# l3 = s.mergeTwoLists([1,2,3,4],[5,6,7,8])
# print l3
