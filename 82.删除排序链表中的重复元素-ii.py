#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (46.67%)
# Likes:    264
# Dislikes: 0
# Total Accepted:    44.3K
# Total Submissions: 93.2K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
# 
# 示例 1:
# 
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 
# 
# 示例 2:
# 
# 输入: 1->1->1->2->3
# 输出: 2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        # dummy.next = head
        fast = head
        slow = dummy
        skip = 0
        while fast:
           
            if not fast.next:
                slow.next = ListNode(fast.val)
                break
            if fast.val == fast.next.val:
                while fast.val == fast.next.val:
                    fast = fast.next
                    if not fast.next:
                        break
                fast = fast.next
                skip = 1
                continue
            else:
                slow.next = ListNode(fast.val)
                fast = fast.next
                slow = slow.next


        return dummy.next
# @lc code=end

