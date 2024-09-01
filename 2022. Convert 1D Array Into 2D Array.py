class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if (m*n) > len(original) or (m*n) < len(original):
            return []

        new = []
        for row in range(m):
            newRow = []
            offset = n*row
            for column in range(n): 
                newRow.append(original[offset+column])
            new.append(newRow)
        return new
