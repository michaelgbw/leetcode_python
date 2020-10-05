#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

# @lc code=start
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        dp_len = [1] * n
        dp_count = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp_len[i] <= dp_len[j]:
                        dp_len[i] = dp_len[j] + 1
                        dp_count[i] = dp_count[j]
                    elif dp_len[i] == dp_len[j] + 1:
                        dp_count[i] += dp_count[j]
        longest = max(dp_len)
        return sum(dp_count[i] for i in range(n) if dp_len[i]==longest )
# @lc code=end

