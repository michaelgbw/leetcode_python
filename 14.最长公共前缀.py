#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (36.59%)
# Likes:    921
# Dislikes: 0
# Total Accepted:    211.5K
# Total Submissions: 577.2K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        pre_str = ''
        doubel_list = []
        for v in strs:
            if v == '':
                return ''
            doubel_list.append([i for i in v])
        for j in range(len(doubel_list[0])):
            for i in range(len(doubel_list)):
                # print(doubel_list[i][j])
                try:
                    doubel_list[i][j]
                except :
                    return pre_str
                if doubel_list[0][j] != doubel_list[i][j]:
                    return pre_str
            
            pre_str += doubel_list[0][j]
        return pre_str 
# @lc code=end

ob = Solution()
print(ob.longestCommonPrefix(["f","f",'fa']))
