class Solution:
    def sortColors(self, nums: List[int]) -> None:
        rearPointer = len(nums)-1
        def lookForSwap(index:int,numberToSwap:int):
            nonlocal rearPointer
            swapped = False
            if nums[index] == numberToSwap and index < rearPointer:
                while swapped == False and index < rearPointer:
                    if nums[rearPointer] < numberToSwap:
                        temp = nums[rearPointer]
                        nums[rearPointer] = nums[index]
                        nums[index] = temp
                        print(nums,"Swapped position",index,"and",rearPointer)
                        rearPointer -= 1
                        swapped = True
    
                    else: 
                        rearPointer -= 1
        for i in range(rearPointer+1): 
            lookForSwap(i,2)
        for i in range(rearPointer+1): 
            lookForSwap(i,1)
