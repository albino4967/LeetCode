class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        else :
            while True :
                if n%4 == 0 :
                    n = n/4
                else :
                    break
            if n == 1 :
                return True
        
        return False
        