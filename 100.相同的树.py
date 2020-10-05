#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# https://leetcode-cn.com/problems/same-tree/description/
#
# algorithms
# Easy (56.81%)
# Likes:    352
# Dislikes: 0
# Total Accepted:    83.8K
# Total Submissions: 146K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# 
# 示例 1:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# 输出: true
# 
# 示例 2:
# 
# 输入:      1          1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# 输出: false
# 
# 
# 示例 3:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# 输出: false
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
    # def isSameTree2(self, p, q):
    #     if p is None or q is None:
    #         return p == q
    #     elif p.val == q.val:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #     return False


    #并发版本
    def isSameTree(self, p, q):

        p_iter = Iterable(p)
        q_iter = Iterable(q)

        try:
            while True:
                p_v = p_iter.next()
                q_v = q_iter.next()
                if p_v != q_v:
                    return False 
        except:
            return True
        return True 


class Iterable(object):
    def __init__(self,p):
        self.p = p
        self.stack = [p]
    def next(self):
        if not self.stack:
            raise StopIteration()
        top = self.stack.pop()
        if top is None:
            return top
        
        self.stack.append(top.left)
        self.stack.append(top.right)
        return top.val
    

# @lc code=end

