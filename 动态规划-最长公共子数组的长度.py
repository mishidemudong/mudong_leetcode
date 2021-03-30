
'''
整体是最长公共子序列相同的框架，这个题目在于是要求是连续的，那么在状态转移方程上有一点改动很关键，不相等则从0开始，
另外需要一个最大值变量来每次迭代完更新最长即可。

'''

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