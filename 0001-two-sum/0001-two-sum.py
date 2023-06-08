class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i, item in enumerate(nums[:-1]) :
            for j, jtem in enumerate(nums[i+1:]) :
                if item + jtem == target :
                    result = [i,j+i+1]
        return result
        
        