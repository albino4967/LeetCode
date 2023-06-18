class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n <= 0:
            return False

        else :
            while True :
                if n%3 == 0 :
                    n = n/3
                else :
                    break
            if n == 1 :
                return True
        
        return False
                    
        