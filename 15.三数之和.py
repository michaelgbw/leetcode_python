#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (26.05%)
# Likes:    1928
# Dislikes: 0
# Total Accepted:    184.7K
# Total Submissions: 705.3K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res =[]
        for i in range(len(nums)):
            if i == 0 or nums[i]>nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if s ==0 :
                        print(l,r)
                        res.append([nums[i],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while r>l and nums[l]==nums[l-1]:
                            l+=1
                        while r>l:
                            r-=1
                    elif s>0:
                        r -=1
                    else :
                        l +=1
            print('++++')
        return res
# @lc code=end
ob = Solution()
print(ob.threeSum([-2,0,1,1,2]))

