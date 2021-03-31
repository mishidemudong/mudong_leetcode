class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        if len(nums) == 1:
            return nums[0]

        m = len(nums)
        # dp = [[0] * (m+1) for _ in range(m +1)]
        dp = [0] * (m)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, m):
            ###重点在状态转移方程，针对当前房屋，要么打劫，要么不打劫
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]