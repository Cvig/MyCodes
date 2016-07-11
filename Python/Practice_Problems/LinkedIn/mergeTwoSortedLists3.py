# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
#This is linked list implementation of merge two sorted lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self,l1,l2):
        spliced = ListNode(0)
        if l1 == None or l2 == None:
            if l1 != None:
                return l1
            elif l2 != None:
                return l2
            else:
                return l1

        #spliced.next = l1 #head of l1 as a node of spliced but what if its a null? So we need to check
        temp = spliced #keep in mind how u assign value, sliced = temp is wrong way
         #lets just keep spliced and we will use temp to identify where is the next element at: l1 or l2?
        while l1 and l2: #if even one is fully iterated, exit, otherwise it means l1 and l2 both have elements
            #till then, keep comparing and adding next reference to be smaller number
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next  #update l1
            else:
                temp.next = l2   #update l2
                l2 = l2.next
            temp = temp.next
        if l1 == None:  #if one of them dont have elements, then check which one is that?
            temp.next = l2  # join remaining l2 to temp
        elif l2 == None:
            temp.next = l1   # join remaining l1 to temp

        return spliced.next
        

