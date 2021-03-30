


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m1 = len(A)
        m2 = len(B)

        dp = [[0] * (m2 + 1) for _ in range(m1 + 1)]

        res = 0
        for i in range(1, m1 + 1):
            for j in range(1, m2 + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0

                res = max(res, dp[i][j])

        return res