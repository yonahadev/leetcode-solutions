class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(numRows-1):
            currentRow = []
            previousRow = rows[i]
            print(previousRow,i)
            for i in range(len(previousRow)):
                if i == 0:
                    currentRow.append(1)
                else: 
                    currentRow.append(previousRow[i]+previousRow[i-1])
                    # currentRow.append(0)
            currentRow.append(1)
            rows.append(currentRow)
        return rows