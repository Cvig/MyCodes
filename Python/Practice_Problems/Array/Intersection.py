#find intersection of two lists of integers
#Cases: lists could be empty
#there could be duplicates in the list
#length may be different, in that case my list could not be bigger than that

class Solution(object):

    def intersection(self, l1, l2):
        """
        :type l1: list of integers
        :type l2: list of integers
        :rtype : list of integers
        """
        l3 =[] #This is initialization of intersection list
        dic_l3 = {} #We will keep a hashmap
        if l1 == None or l2 == None: #if either of them is empty
            return l3 #no element in intersection
        #if both have elements
        #iterate first list
        for i in range(len(l1)):
            if l1[i] in dic_l3:
                dic_l3[l1[i]] +=1 #add 1 to the count
            else:
                dic_l3[l1[i]] = 1   #add the element as the key
        #Now iterate the next list
        for j in range(len(l2)):
            if l2[j] in dic_l3: #if this is a key already
                l3.append(l2[j]) #add the element to the result
                dic_l3[l2[j]] -= 1 #decrement 1
        return l3

#Test
'''
l1 =[5,8]
l2 =[8,0]
s = Solution()
r = s.intersection(l1,l2)
print r
'''