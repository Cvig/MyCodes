#The challenge is to find first fibonacci number which is prime after the given number
#e.g. if 10 is the given number, prime fibonacci number after 10 is 13
import math

class Solution(object):
    def PrimeFibonacciNumber(self, abovethis):
        if abovethis <2:
            return 2
        else:
            return self.getfib(abovethis)

    def getfib(self,number): #let number = 10
        fib = [0,1,1]
        while fib[len(fib)-1] <= number: #cur is last element is fibonacci sequence
            fib.append(fib[len(fib)-1] + fib[len(fib)-2])

        while self.prime(fib[len(fib)-1]) == False:
            fib.append(fib[len(fib)-1]+fib[len(fib)-2])
        return fib[len(fib)-1]

    def prime(self,num):
        for i in xrange(2, int(math.sqrt(num))):
            if num%i ==0:
                return False
        return True

s = Solution()
r= s.PrimeFibonacciNumber(2904353)
print r