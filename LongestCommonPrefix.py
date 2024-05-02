class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestLength = 201
        commonPrefix = ""
        listLength = len(strs)
        for word in strs: #finds the length of the shortest word
            length = len(word)
            if length < shortestLength: 
                shortestLength = length
        for i in range(shortestLength):
            matchCount = 0
            print(i)
            for string in strs: 
                if string[i] == strs[0][i]:
                    matchCount += 1
            if matchCount != listLength: 
                return commonPrefix
            else: 
                commonPrefix += strs[0][i]
        return commonPrefix
