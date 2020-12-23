#
# @lc app=leetcode.cn id=26 lang=python3
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        s = 0
        for k in range(1,len(nums)):
            if nums[s] != nums[k]:
                s+=1
                nums[s] = nums[k]
        return s+1
            
# obj = Solution()
# a = obj.removeDuplicates([1,1,2]) 
# print(a) 
 
# @lc code=end

