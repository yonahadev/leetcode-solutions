class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sumTotal = 0
        happiness.sort()
        for i in range(k): 
            current = happiness[-1]
            happiness.pop()
            sumTotal += max(0,current-i)
        return sumTotal
