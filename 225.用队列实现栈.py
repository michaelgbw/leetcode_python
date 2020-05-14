#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
# https://leetcode-cn.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (64.15%)
# Likes:    171
# Dislikes: 0
# Total Accepted:    51.6K
# Total Submissions: 79.8K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# 使用队列实现栈的下列操作：
# 
# 
# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
# 
# 
# 注意:
# 
# 
# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty
# 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
# 
# 
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
 
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)
 
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1[0])
            self.queue1 = self.queue1[1:]
 
            
        # print self.queue1, self.queue2
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        # print self.queue1, self.queue2
        top = self.queue1[0]
        self.queue1, self.queue2 = self.queue2, []
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1[0])
            self.queue1 = self.queue1[1:]
        return top
            
 
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue1[0]
        
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue1 and not self.queue2




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

