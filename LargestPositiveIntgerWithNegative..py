class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hashMap = {} #map of absolute value: (posValuePresent,negValuePresent)
        highest = -1
        for num in nums:
            absolute = abs(num)
            if absolute not in hashMap: 
                if num > 0:
                    hashMap[absolute] = (True,False)
                if num < 0:
                    hashMap[absolute] = (False,True)
            else: 
                print(num)
                if num > 0:
                    hashMap[absolute] = (True,hashMap[absolute][1])
                if num < 0: 
                    hashMap[absolute] = (hashMap[absolute][0],True)
        for key,value in hashMap.items(): 
            if value == (True,True) and key > highest:
                highest = key
        return highest
