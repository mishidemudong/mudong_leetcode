




class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        def dp(n):

            if n in memo.keys():
                return memo[n]

            if n == 0:
                return 0

            if n < 0:
                return -1

            res = 999999999
            for coin in coins:
                sub_res = dp(n - coin)
                if sub_res == -1:
                    continue
                res = min(res, sub_res + 1)

            if res != 999999999:
                memo[n] = res
            else:
                memo[n] = -1

            return memo[n]

        return dp(amount)