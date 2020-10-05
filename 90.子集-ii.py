#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
# result = []
# def backtrack(路径, 选择列表):
#     if 满足结束条件:
#         result.add(路径)
#         return
    
#     for 选择 in 选择列表:
#         做选择
#         backtrack(路径, 新的选择列表)
#         撤销选择


class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        # if len(nums) <= 1:
        #     res.append(nums)
        #     return res
        
        def df(path, begin):
            res.append(path[:])
            for i in range(begin, len(nums)):
                if i>begin and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                df(path, i+1)
                path.pop()

        
        df([],0)
    
        return res

# obj = Solution()
# nums = [0]
# print(obj.subsetsWithDup(nums))

        

# @lc code=end

