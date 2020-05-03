#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (52.86%)
# Likes:    667
# Dislikes: 0
# Total Accepted:    100.9K
# Total Submissions: 189.7K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 示例:
# 
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
    def letterCombinations(self, digits):
        d_to_s = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
        
        
        arr = [v for k,v in enumerate(digits)]
        def add_data(arr):
            if len(arr) == 0:
                return
            if len(self.res) == 0:
                for one in d_to_s[arr[0]]:
                    self.res.append(one)
            else:
                res_len = len(self.res)
                for i in range(res_len):
                    for one in d_to_s[arr[0]]:
                        self.res.append(self.res[i] + one)

                
                self.res = self.res[res_len:]
                
                
            add_data(arr[1:])
            
        add_data(arr)
        return self.res
# @lc code=end
ob = Solution()
print(ob.letterCombinations('232'))

