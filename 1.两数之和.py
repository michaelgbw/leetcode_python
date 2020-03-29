#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        a = 0
        # nums = sorted(nums)
        for k,v in enumerate(nums):
            a = v
            for k1,v1 in enumerate(nums[k+1:],start=k+1):
                if a+v1 == target:
                    res_list = [k,k1]
        return res_list

a = Solution().twoSum([3,2,4], 6)
# print(a)
# @lc code=end

