#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (33.40%)
# Likes:    3342
# Dislikes: 0
# Total Accepted:    399.6K
# Total Submissions: 1.2M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s):
        word_index = {}
        begin =0
        res_len = 0
        for k,v in enumerate(s):
            if v in word_index and begin <= word_index[v]:
                begin = word_index[v] +1
            
            word_index[v] = k
            res_len = max(res_len,(k - begin + 1))
        return res_len
# @lc code=end

ob = Solution()
res = ob.lengthOfLongestSubstring('bbtablud')
print(res)

