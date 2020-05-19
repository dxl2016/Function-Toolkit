class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n < 0:
            return 1 / self.myPow(x, -n)
        else:      
            p = 1
            base = x

            while n != 0:
                if n % 2 == 1:
                    p = p * base

                base *= base
                n = n // 2

            return p
