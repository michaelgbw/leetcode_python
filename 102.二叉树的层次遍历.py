#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (61.22%)
# Likes:    463
# Dislikes: 0
# Total Accepted:    112.5K
# Total Submissions: 182.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 
# 
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        queue = [root]
        
        res = []
        if root is None:
            return []

        while len(queue) != 0:
            number_flag = len(queue)
            i = 0
            rank_res = []
            while i < number_flag:
                tmp = queue.pop(0)
                rank_res.append(tmp.val)
                # if tmp.left or tmp.right:
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
                i += 1
            res.append(rank_res)
        return res

# obj = Solution()
# obj.levelOrder
        
            
# @lc code=end

