#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#worst
# class Solution:
#     def isValidBST(self, root):
#         if root == None:
#             return True
#         l = self.getRes(root)
#         for i in range(1,len(l)):
#             if l[i-1].val >= l[i].val:
#                 return False
#         return True
#     def getRes(self, root, res=[]):
#         if root == None:
#             return []
#         left = self.getRes(root.left)            
#         right = self.getRes(root.right)
#         return left + [root] + right

class Solution:
    def isValidBST(self, root):
        if root == None:
            return True
        stack = []
        pre = None
        while root is not None or len(stack) > 0:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop(-1)
                if pre != None:
                    if pre.val >= root.val:
                        return False
                pre = root
                root = root.right
                
        return True
                

# @lc code=end

