#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (67.99%)
# Likes:    335
# Dislikes: 0
# Total Accepted:    39K
# Total Submissions: 56.7K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给定一个二叉树，原地将它展开为链表。
# 
# 例如，给定二叉树
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 将其展开为：
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# not in-place
# class Solution:
#     def flatten(self, root):
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         if not root:
#             pass
#         root_list = TreeNode(root.val)
#         stack = [root]
#         res = []
#         while len(stack) != 0:
#             a = stack.pop()
#             res.append(a.val)
#             if a.right is not None:
#                 stack.append(a.right)
            
#             if a.left is not None:
#                 stack.append(a.left)
            
#         print(res)
#         for one in res:
#             root_list.left = None
#             root_list.right = TreeNode(one,left=None)
#             root_list = root_list.right

class Solution:
    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        #左树接右树
        if root.left:
            tmp_right = root.right
            root.right = root.left
            root.left = None
            #右树接最后
            while root.right:
                root = root.right
            root.right = tmp_right
# @lc code=end


