#This solution is accepted on Leetcode
#You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #if one of the lists is empty
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        #declare empty list and initialize it to 0
        dummy = ListNode(0)
        l3 = dummy  #very important to have a dummy here, otherwise your list will not be saved
        #initialize carry to 0
        carry = 0
        #We need to add from left to right as least significant digit is left-most
        #We need to take care of the carry as we move ahead
        while l1 and l2: #while there are digits remaining in both

            num = carry + l1.val + l2.val # addition of corresponding first values of l1 and l2
            if num > 9: #assuming only non-negative numbers and no sign, if number is 10 or greater, there is a carry
                carry = 1
                num = num-10 #this value needs to be added to final list
            else:
                carry = 0
            node = ListNode(num)
            l3.next = node #add the number into resultant list
            #advance both l1 and l2
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        if l1 == None:
            while l2:
                num = carry + l2.val
                if num > 9:
                    carry = 1
                    num = num -10
                else:
                    carry = 0
                node = ListNode(num)
                l3.next = node
                l3 = l3.next
                l2 = l2.next
        elif l2 == None:
            while l1:
                num = carry + l1.val
                if num > 9:
                    carry = 1
                    num = num -10
                else:
                    carry = 0
                node = ListNode(num)
                l3.next = node
                l3 = l3.next
                l1 = l1.next #loop can run forever if u dont write this
        if carry:  #what about the last carry??
            node = ListNode(carry)
            l3.next = node
        return dummy.next