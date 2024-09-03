class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string = ""
        for char in s: 
            asciiValue = ord(char)
            finalValue = asciiValue - 96
            string += str(finalValue)
        for i in range(k): 
            total = 0
            for char in string:
                total += int(char)
            string = str(total)
        return int(string)
