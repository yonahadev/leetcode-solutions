class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index,value in enumerate(nums):
            targetToFind = target-value 
            if index >= 1:           
                if targetToFind in map: 
                    return [map[targetToFind],index]
            if value not in map:
                map[value] = index
