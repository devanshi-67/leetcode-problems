class Solution:
    def generate(self,numsRows):
        result = []

        for i in range(numsRows):
            row = [1] * (i + 1)

            for j in range(1,i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            result.append(row)

        return result
                                                                  
        