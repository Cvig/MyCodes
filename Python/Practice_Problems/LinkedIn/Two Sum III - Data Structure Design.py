'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers whose sum is equal to the value.
'''


class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.numsCount = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        # there could be duplicates in this array so better to use hashmap consisting of value and its count instead of storing each element separately because we are not interested in indices of twoSum, but just whether two elements sum to value or not.
        if number in self.numsCount:
            self.numsCount[number] +=1
        else:
            self.numsCount[number] = 1 #check self. kind of errors



    def find(self, value):
        """
        Find if there exists any pair of numbers whose sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.numsCount:
            first = key
            second = value - first
            if first == second: #if they are equal, that will be checked earlier
                if self.numsCount[key] >1:
                    return True
            elif second in self.numsCount: #else if they are not equal, do use else if and not just if
                return True
        return False


print len([])
# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)