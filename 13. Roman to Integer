class Solution:
    def romanToInt(self, s: str) -> int:
        stack = []
        total = 0
        numerals = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        for numeral in s:
            num = numerals[numeral] 
            if len(stack) > 0:
                preceeding = stack.pop()
                if num > preceeding:
                    total += (num-preceeding)
                    continue
                else: 
                    total += preceeding
                    stack.append(num)
            else:
                stack.append(num)
        if len(stack) > 0:
            total += stack[-1]
        return total
