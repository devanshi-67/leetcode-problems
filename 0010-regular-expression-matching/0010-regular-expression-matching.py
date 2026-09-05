class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def solve(i , j):
            if (i , j) in memo:
                return memo[(i , j)]

            if j == len(p):
                return i == len(s)

            first_match = (
                 i < len(s) and 
                 (s[i] == p[j] or p[j] == '.')
                 )

            if j + 1 < len(p) and p[j + 1] == '*':
                answer = solve(i,j + 2) or (
                    first_match and solve(i + 1,j)
                    )
            else:
                answer = first_match and solve(i + 1,j + 1)

            memo[(i, j)] = answer
            return answer 

        return solve(0,0)
        