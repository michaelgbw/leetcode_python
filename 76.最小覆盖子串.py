#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (35.58%)
# Likes:    416
# Dislikes: 0
# Total Accepted:    32.8K
# Total Submissions: 92.2K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
# 
# 示例：
# 
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 
# 说明：
# 
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
#

# @lc code=start
class Solution:
    def minWindow(self, s, t):
        from collections import Counter
        t_len = len(t)
        if len(s) < t_len:
            return ''
        mem = Counter(t)
        min_l = 0
        min_r = len(s) + 1

        l = 0
        for r,v in enumerate(s):
            if mem[v] > 0: #存在并且没有被减过
                t_len -= 1
            # print('mem',mem)

            mem[v] -= 1
            if t_len == 0:
                while mem[s[l]] < 0:
                    mem[s[l]] += 1
                    l+= 1
                if r - l <= min_r - min_l:
                    min_r = r
                    min_l = l
                
                mem[s[l]] += 1
                t_len += 1
                l += 1
            
        return '' if min_r == len(s) + 1 else s[min_l:min_r + 1]
                


        
# @lc code=end
s = 'abc'
t = 'c'
ob = Solution()
print(ob.minWindow(s,t))

