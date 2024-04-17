#using dictionary
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                return True
            else: 
                hashMap[num] = True
        return False
#using set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            else: 
                numSet.add(num)
        return False
