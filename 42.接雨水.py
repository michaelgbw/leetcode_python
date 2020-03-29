#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (49.33%)
# Likes:    951
# Dislikes: 0
# Total Accepted:    66.2K
# Total Submissions: 133.5K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height):
        h1 = 0
        h2 = 0
        area = 0
        if len(height) == 1:
            return 0
        for i in range(len(height)):
            h1 = max(h1,height[i])
            h2 = max(h2,height[-i-1])
            area = area + h1 + h2 - height[i]
            print('area',area)
        
        print("len(height) * h1",len(height) * h1)
        return area - len(height) * h1
# @lc code=end
ob = Solution()
print(ob.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

