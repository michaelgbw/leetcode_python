#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (74.44%)
# Likes:    709
# Dislikes: 0
# Total Accepted:    127.2K
# Total Submissions: 167.3K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <=1:
            return [nums]
        
        result = [[nums[0]]]
        print(result)
        index = 1
        while index < len(nums):
            tmp = []
            for perm in result:
                for i in range(index+1):
                    tmp.append(perm[:i] + [nums[index]] + perm[i:])
            result = tmp
            index += 1
            print(result)

        
        return result
# @lc code=end

