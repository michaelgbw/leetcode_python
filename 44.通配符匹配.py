#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#
# https://leetcode-cn.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (26.98%)
# Likes:    335
# Dislikes: 0
# Total Accepted:    28.3K
# Total Submissions: 102.6K
# Testcase Example:  '"aa"\n"a"'
#
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
# 
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 
# 
# 两个字符串完全匹配才算匹配成功。
# 
# 说明:
# 
# 
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
# 
# 
# 示例 1:
# 
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 
# 示例 2:
# 
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 
# 
# 示例 3:
# 
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 
# 
# 示例 4:
# 
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 
# 
# 示例 5:
# 
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false
# 
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls = len(s)
        lp = len(p)
        dp = [[False for _ in range(lp+1)] for _ in range(ls+1)]
        dp[0][0] = True
        #首先填写第一行，当p为星号时，即当p的子串最后一个为星时，记为True
        for i in range(1,lp+1):
            if p[i-1]=='*':
                #为什么要用i-1，j-1呢，因为我们填表是填（传递）答案，判断字符要判断答案之前的两个子序列    
                dp[0][i]=dp[0][i-1]
        print(dp[0])
        for i in range(1,ls+1):
            for j in range(1,lp+1):
                if p[j-1]=='*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                    #这里为什么可以继承两个值呢，第一个表示星包含此此时s列加入的这个字母
                    #第二个表示 星 代表空字符，即多了个星出来，那么这个星代表空字符            
                else:
                    dp[i][j] = (s[i-1]==p[j-1] or p[j-1]=='?') and dp[i-1][j-1]
                    #这里第一项好理解，第二项什么意思呢？
                    #指的是前序要True，那么当前s,p才能True
            print(dp[i])

                 
        return dp[ls][lp]

obj = Solution()
s = 'adceb'
p = '*d*b'
obj.isMatch(s, p)
# @lc code=end

