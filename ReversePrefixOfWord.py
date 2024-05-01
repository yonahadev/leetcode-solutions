class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix = ""
        for index in range(len(word)): 
            char = word[index]
            print(char,index)
            if char == ch: 
                prefix = word[0:index+1]
                break
        print(prefix)
        for index in range(len(prefix)):
            reverseIndex = len(prefix)-index-1
            word = list(word)
            word[index] = prefix[reverseIndex]
        word = "".join(word)
        return word
