#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (60.76%)
# Likes:    257
# Dislikes: 0
# Total Accepted:    55.7K
# Total Submissions: 90.6K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 说明：
# 
# 
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []
        # self.candidates = []
    def combinationSum2(self, candidates, target):
        # self.candidates = candidates
        candidates.sort()
        candidates.append(-1)
        # len_candidates = len(candidates)
        
        def getone(candidates,sublist, target, last):
            
            if target == 0:
                self.res.append(sublist)
            if target < candidates[0]:
                return 
            for i in range(len(candidates)):
                if candidates[i] > target:
                    return 
                if candidates[i] < last:
                    continue
                getone(candidates[i+1:], sublist + '|' + str(candidates[i]), target-candidates[i], candidates[i])
        
        getone(candidates, '', target, 0)
        

        self.res = list(set(self.res))
        res = []
        for one in self.res:
            res.append([ int(i) for i in one[1:].split('|')])
        return res
# # @lc code=end

candidates = [2,5,2,1,2]
target = 5
obj = Solution()
obj.combinationSum2(candidates, target)


