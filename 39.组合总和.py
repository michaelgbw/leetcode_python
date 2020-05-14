#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (68.58%)
# Likes:    656
# Dislikes: 0
# Total Accepted:    90.8K
# Total Submissions: 131.8K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的数字可以无限制重复被选取。
# 
# 说明：
# 
# 
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
        self.candidates = []
    def combinationSum(self, candidates, target):
        self.candidates = candidates
        self.candidates.sort()
        # len_candidates = len(candidates)
        
        def getone(sublist, target, last):
            if target == 0:
                self.res.append(sublist)
            if target < self.candidates[0]:
                return 
            for one in self.candidates:
                if one > target:
                    return 
                if one < last:
                    continue
                getone(sublist + [one], target-one, one)
        
        getone([], target, 0)
        
        return self.res
                    
# @lc code=end
obj = Solution()
res = obj.combinationSum([2,3,6,7],7)
print(res)

