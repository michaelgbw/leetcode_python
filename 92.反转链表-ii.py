#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (49.41%)
# Likes:    359
# Dislikes: 0
# Total Accepted:    48.3K
# Total Submissions: 96.8K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        if not head:
            return None
        
        p = dummy
        
        #慢指针指到m-1处
        for _ in range(m-1):
            p = p.next

        pre,cur = p,p.next
        for _ in range(m, n+1):
            node_next = cur.next
            cur.next = pre
            pre = cur
            cur = node_next
        # print('pre.val', pre.val)
        # print('cur.val', cur.val)

        p.next.next = cur
        p.next = pre

        return dummy.next
        
# @lc code=end

