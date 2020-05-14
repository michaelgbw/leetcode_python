#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
# https://leetcode-cn.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (37.62%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    43K
# Total Submissions: 113.7K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 
# 
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 
# 
# 示例 1:
# 
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j_len = len(matrix)
        if j_len == 0:
            return False
        i_len = len(matrix[0])
        if i_len == 0:
            return False
        
        j_right = j_len -1
        j_left = 0
        i_right = i_len -1
        i_left = 0
        is_set = False
        mid_j = 0
        while j_right >= j_left:
            mid_j = (j_right+j_left) // 2
            if matrix[mid_j][0] > target:
                j_right = mid_j -1
            elif matrix[mid_j][i_len-1] < target:
                j_left = mid_j + 1
        
            elif matrix[mid_j][0] <= target and matrix[mid_j][i_len-1] >= target:
                is_set = True
                break
            else:
                return False
        if not is_set:
            return False
        while i_left <= i_right:
            mid = (i_left + i_right)  // 2
            if target < matrix[mid_j][mid]:
                i_right = mid - 1
            elif target > matrix[mid_j][mid]:
                i_left = mid + 1
            else:
                return True
        return False



# if matrix == []:
#     return False
# m, n = len(matrix), len(matrix[0])
# low = 0
# high = m * n
# while low < high:
#     mid = (low + high) // 2
#     if matrix[mid // n][mid % n] == target:
#         return True
#     elif matrix[mid // n][mid % n] < target:
#         low = mid + 1
#     else:
#         high = mid
# return False
        
# @lc code=end

