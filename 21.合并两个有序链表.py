#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (60.42%)
# Likes:    957
# Dislikes: 0
# Total Accepted:    229.9K
# Total Submissions: 376.7K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        new_node = ListNode(0)
        first = new_node
        new_node.next = None

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                new_node.next = l1
                l1 = l1.next
            else :
                new_node.next = l2
                l2 = l2.next
            new_node = new_node.next
        
        if l1 == None:
            new_node.next = l2
        elif l2 == None:
            new_node.next = l1
        return first.next
        
        
        
# @lc code=end

