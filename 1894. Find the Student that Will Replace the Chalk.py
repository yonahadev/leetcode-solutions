class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = 0
        for amount in chalk:
            total += amount
        quotient = k//total    
        
        k -= quotient*total

        student = 0
        while True: 
            chalkAmount = chalk[student]
            if chalkAmount > k: 
                return student
            k -= chalkAmount
            if student == len(chalk)-1:
                student = 0
            else: 
                student += 1
