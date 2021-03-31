
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        sorted_nums = sorted(nums, reverse=False)

        dp = [1] * (len(sorted_nums))
        res = 1
        for i in range(1, len(sorted_nums)):
            # for j in range(1, len(sorted_nums)+1):
            if sorted_nums[i] == sorted_nums[ i -1 ] +1:
                dp[i] = dp[ i -1] + 1
            else:
                dp[i] = 1

            res = max(res, dp[i])

        return res


        #官网字典解法
        longest_streak = 0
        dp_set = set(nums)

        for num in nums:
            if num - 1 not in dp_set:
                current_num = num
                max_l = 1
                while current_num + 1 in dp_set:
                    current_num += 1
                    max_l += 1

                longest_streak = max(max_l, current_num)

        return longest_streak