class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        p = x
        #Most intuitive way is x^n = x.x.x.....n times but you need to take care of odd and even cases
        #corner cases
        if n==1:
            return x
        if x==0:
            return 0 #this is undefined if n is 0 as well
        if x==1 or n==0:
            return 1.0
        if n<0:
            return 1/self.myPow(x,-n)

        p = pow(x,n/2) 

        if n%2 ==0: #even here it should be n not x
            return p*p
        else:
            return p*p*x #for odd, you need to multiply extra x