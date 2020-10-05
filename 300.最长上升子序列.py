#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#


# @lc code=start
class Solution:
    # 一般的DP算法
    # def lengthOfLIS(self, nums):
    #     n = len(nums)
    #     if n <= 0:
    #         return 0
    #     dp = [1] * n
    #     ans = 1
    #     for i in range(n):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i],dp[j]+1)
    #                 ans = max(ans,dp[i])
        
    #     return ans

    # 贪心算法
    def lengthOfLIS(self,nums):
        n = len(nums)
        if n <= 0: return 0
        a = [nums[0]]
        for i in range(1,n):
            if nums[i] > a[-1]:
                a.append(nums[i])
            else:
                if nums[i] < a[0]:
                    a[0] = nums[i]
                else:
                    # position = self.binarySearch(a,nums[i],0,len(a)-1)
                    position = self.binarySearch(a,nums[i])
                    a[position] = nums[i]
        print(a)
        return len(a)
    
    def binarySearch(self,nums,num):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if num > nums[mid]:
                left = mid + 1
            elif num < nums[mid]:
                right = mid - 1
            else:
                return mid
        return left   

      
# @lc code=end

