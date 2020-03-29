class myStack(object):
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


class myQueue(object):
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
            return self.stack.pop(0)
        else:
            return False
    def is_empty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.stack)

    def peek(self):
        if self.stack:
            return self.stack[-1]

