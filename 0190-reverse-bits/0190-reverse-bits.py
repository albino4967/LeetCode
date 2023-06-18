class Solution:
    def reverseBits(self, n: int) -> int:
        n = '{:032b}'.format(n)
        reverse_bit = []
        for i in reversed(n) :
            reverse_bit.append(i)
        return int(''.join(reverse_bit), 2)
            
