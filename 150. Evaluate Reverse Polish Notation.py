class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] #lambda functions are cool
        operatorMapping = {"+":lambda x,y: x+y,"-": lambda x,y: x-y, "*": lambda x,y: x*y,"/":lambda x,y:int(x/y)} #int(x/y) truncates to 0
        for token in tokens: 
            if token in operatorMapping:
                num1 = stack.pop()
                num2 = stack.pop()
                result = operatorMapping[token](num2,num1)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]
