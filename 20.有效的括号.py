#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (41.15%)
# Likes:    1470
# Dislikes: 0
# Total Accepted:    238.9K
# Total Submissions: 579K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#

# @lc code=start


class Solution(object):
    def __init__(self,limit=10):
        self.stack = []
        self.stack_limit = limit
    
    def push(self, data):
        if self.stack_limit < len(self.stack):
            return False
        else:
            self.stack.append(data)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return False
    def is_empty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.stack)

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def isValid(self, s):
        str_len = len(s)
        self.stack_limit = str_len
        
        for one in s:
            is_bingo = 0
            if self.is_empty():
                self.push(one)
            else:
                top = self.peek()
                if top == '{':
                    if one == '}':
                        is_bingo = 1
                if top == '[':
                    if one == ']':
                        is_bingo = 1
                if top == '(':
                    if one == ')':
                        is_bingo = 1
                if is_bingo == 1:
                    self.pop()
                else:
                    self.push(one)
        if self.size() == 0:
            return True
        else:
            return False

ob = Solution()
s = '(())'
print(ob.isValid(s))
# @lc code=end

