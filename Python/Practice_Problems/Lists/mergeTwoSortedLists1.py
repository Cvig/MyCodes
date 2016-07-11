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

