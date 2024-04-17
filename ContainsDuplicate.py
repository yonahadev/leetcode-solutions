class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        for letter in s:
            if letter not in mapS:
                mapS[letter] = 1
            else:
                mapS[letter] += 1
        for letter in t: 
            if letter not in mapT:
                mapT[letter] = 1
            else: 
                mapT[letter] += 1
        if mapT == mapS:
            return True
        else: 
            return False
