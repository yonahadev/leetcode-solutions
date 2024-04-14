class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def createNewList(list:List[int],start:int,end:int) -> List[int]: 
            newList = []
            for i in range(start,end+1): 
                newList.append(list[i])
            return newList

        relativeIndex = 0

        while True:
            if len(nums) == 0:
                return -1

            length = len(nums)
            middleIndex = (length-1)//2 
            middleNumber = nums[middleIndex]

            if middleNumber == target: 
                return middleIndex+relativeIndex
            elif middleNumber < target: 
                nums = createNewList(nums,middleIndex+1,length-1)
                relativeIndex += middleIndex+1
            elif middleNumber > target: 
                nums = createNewList(nums,0,middleIndex-1)
