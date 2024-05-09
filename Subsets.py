class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        currentSubset = []

        def dfs(i:int):
            if i == len(nums): #index too large = traversed all of that branch
                subsets.append(currentSubset.copy()) #copy as python objects by reference
                return
            
            currentSubset.append(nums[i])
            dfs(i+1) #call to get case without empty slot
            currentSubset.pop()
            dfs(i+1) #call to get case with an empty index
        
        dfs(0) #starts backtrack on first element

        return subsets
