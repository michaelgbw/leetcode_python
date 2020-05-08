#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#
# https://leetcode-cn.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (54.11%)
# Likes:    128
# Dislikes: 0
# Total Accepted:    9.7K
# Total Submissions: 17.5K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
# 
# update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。
# 
# 示例:
# 
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# 
# 
# 说明:
# 
# 
# 数组仅可以在 update 函数下进行修改。
# 你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。
# 
# 
#

# @lc code=start
class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (self.n << 1)
        # [0, 0, 0, 0, 0, 0]
        #分为两段
        for i in range(self.n, self.n << 1):
            self.tree[i] = nums[i - self.n]
        print(self.tree)
        for i in range(self.n - 1, 0, -1):
            print('self.tree[i << 1]',self.tree[i << 1])
            print('self.tree[i << 1 + 1]',self.tree[(i << 1) + 1])
            self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) + 1]
        print(self.tree)
    def update(self, i: int, val: int) -> None:
        i += self.n
        val -= self.tree[i]
        while i:
            self.tree[i] += val
            i >>= 1
    def sumRange(self, i: int, j: int) -> int:
        i += self.n
        j += self.n
        res = 0
        while i <= j:
            print('i',i)
            print('j',j)
            if i & 1:
                #奇数
                res += self.tree[i]
                i += 1
            if not j & 1:
                #偶数
                res += self.tree[j]
                j -= 1
            i >>= 1
            j >>= 1
        return res
        


# Your NumArray object will be instantiated and called as such:
nums = [1,2,3,4,5,6,7,8]
i = 0
j = 7
obj = NumArray(nums)
# obj.update(i,val)
param_2 = obj.sumRange(i,j)
print(param_2)
# @lc code=end

