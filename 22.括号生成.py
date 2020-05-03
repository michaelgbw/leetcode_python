#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (73.59%)
# Likes:    843
# Dislikes: 0
# Total Accepted:    94.9K
# Total Submissions: 128.6K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
# 
# 例如，给出 n = 3，生成结果为：
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n):
        res = []
    
        def backtrack(pre, left, right):
            if len(pre) == 2 * n:
                res.append(pre)
                return
            if left < n:
                backtrack(pre + '(', left+1, right)
            if right < left:
                backtrack(pre + ')' , left, right+1)
        
        backtrack('',0,0)
        return res

ob = Solution()
res = ob.generateParenthesis(4)
print(res)
# @lc code=end

