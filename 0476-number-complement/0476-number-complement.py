class Solution:
    def findComplement(self, num: int) -> int:
        print(bin(num)[2:])
        complement = []
        for i, item in enumerate(bin(num)[2:]) :
            if item == "1" :
                complement += "0"
            else :
                complement += "1"
        return int("".join(complement), 2)
                