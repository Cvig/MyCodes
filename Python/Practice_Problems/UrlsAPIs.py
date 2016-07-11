#Author: Chetna Vig

''' Problem statement:
Take a list of list of strings and concatenate them into a url
eg., Given [['www'], ['paypal', 'paypal-hub'],['com']]
Result should be:
www.paypal.com
www.paypal-hub.com

Note: list of strings could be of variable length
'''

'''
genUrls class have two major solutions to the problem and one solution is just another
form of Brute force but using two functions(genUrls2 and recGenUrls)
Major solutions are:
1. genUrls1 (Brute-Force) and
2. genUrls3 (Recursive)
The recursive solution has benefit when we want to display urls on-the-fly and we don't have to
wait to get the complete set of Urls.
'''

class genUrls(object):

    '''
        This function takes in a list of list and returns the list of urls
        Solution1 : Brute Force
        Time complexity : O(m*n*o*p)where m, n, o and p are number of elements in each list inside given list
        Space Complexity : O(m*n*o*p) which is number of urls generated
    '''

    def genUrls1(self, lst):
        '''

        :param list[lst[str]]
        :return: lst[str]
        '''
        if len(lst) == 0:
            return lst
        m, n, o, p = len(lst[0]), len(lst[1]), len(lst[2]), len(lst[3])
        urls = []
        for i in range(m):
            for j in range(n):
                for k in range(o):
                    for l in range(p):
                        urls.append(lst[0][i] + '.' + lst[1][j] + '.' + lst[2][k] + '.' + lst[3][l])
        return urls

    '''
        Solution2 : Another implementation of Brute force twisted
        Time complexity : O(m*n*o*p)where m, n, o and p are number of elements in each list inside given list
        Space Complexity : O(m*n*o*p)which is number of urls generated
    '''

    def genUrls2(self, lst):
        '''

        :param list[lst[str]]
        :return: lst[str]
        '''
        if len(lst) == 0:
            return lst
        urls = lst[0]
        for i in range(1,len(lst)):
            urls = self.recGenUrls(urls, lst[i])
        return urls

    def recGenUrls(self, strList, lst):
        if len(lst) == 0:
            return strList
        urls = []
        for each1 in strList:
            for each2 in lst:
                urls.append(each1 + '.' + each2)
        return urls

    '''
        Solution3 : Recursive Calls
        Time complexity : O(m*n*o*p)where m, n, o and p are number of elements in each list inside given list
        Space Complexity : O(m*n*o*p)which is number of urls generated
        This solution is useful if we want to complete one url before moving onto the another one.
        This is big advantage of using recursion here.
    '''
    def genUrls3(self, lst):
        '''

        :param list[lst[str]]
        :return: lst[str]
        '''
        if len(lst) == 0:
            return lst
        urlList = []
        self.recursive(lst,0, '', urlList)
        return urlList

    def recursive(self, lst, index, str, urlList):
        if (index > len(lst)-1):
            urlList.append(str[1:])
            return
        for each in lst[index]:
            self.recursive(lst, index+1, str + '.' + each, urlList)


#Test Class which prints the output, can add more features to test, this is just a structure
class testGenUrls():

    def testGenUrl1(self, lst):

        s = genUrls()
        a = s.genUrls1(lst)
        print a
        print len(a)
        num = 1
        for each in lst:
            num *= len(each)
        if len(a) == num:
            print 'Test Passed'

    def testGenUrl2(self, lst):

        s = genUrls()
        a = s.genUrls2(lst)
        print a
        print len(a)
        num = 1
        for each in lst:
            num *= len(each)
        if len(a) == num:
            print 'Test Passed'

    def testGenUrl3(self, lst):

        s = genUrls()
        a = s.genUrls3(lst)
        print a
        print len(a)
        num = 1
        for each in lst:
            num *= len(each)
        if len(a) == num:
            print 'Test Passed'

#Test
'''
lst = [['www','http','https'], ['api','games'], ['paypal', 'paypal-hub','paypal-stuff'],['com','org','co']]
s = testGenUrls()
s.testGenUrl1(lst)
s.testGenUrl2(lst)
s.testGenUrl3(lst)
'''


