#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (38.04%)
# Likes:    756
# Dislikes: 0
# Total Accepted:    145.6K
# Total Submissions: 380.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 
# 示例：
# 
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 
# 
# 说明：
# 
# 给定的 n 保证是有效的。
# 
# 进阶：
# 
# 你能尝试使用一趟扫描实现吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#还有种方法就是不用快慢指针，直接循环两遍，假设长度为k，那么第一次遍历k-1,到头，第二次遍历k+1,到0时候，就找到了要删除的节点的前一个节点
class Solution
    def removeNthFromEnd(self, head, n):
        node_list = []
        head0 = ListNode(0)
        head0.next = head
        normal = head0
        slow = head0

        for _ in range(n):
            normal = normal.next
        while normal.next:
            slow = slow.next
            normal = normal.next
        # node = slow.next
        # slow.next = node.next
        # node.next = node
        slow.next = slow.next.next
        return head0.next



# @lc code=end

