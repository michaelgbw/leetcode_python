#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
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
# @lc code=end

