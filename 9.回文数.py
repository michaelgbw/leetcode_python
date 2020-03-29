#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (57.21%)
# Likes:    973
# Dislikes: 0
# Total Accepted:    278.6K
# Total Submissions: 486.9K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 
# 示例 1:
# 
# 输入: 121
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 
# 
# 示例 3:
# 
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 
# 
# 进阶:
# 
# 你能不将整数转为字符串来解决这个问题吗？
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, x):
        prev_x = x
        inve_x = 0
        while prev_x > 0:
            inve_x = inve_x * 10 + (prev_x % 10)
            prev_x = prev_x // 10
            
        return inve_x == x
        
# @lc code=end
s = Solution()
s.isPalindrome(11)

