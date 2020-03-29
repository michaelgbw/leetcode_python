####python自带的：https://blog.csdn.net/qiwsir/article/details/36715163

class Node:  
    def __init__(self,item=None,left=None,right=None):  
        self.item = item  
        self.lchild = left
        self.rchild = right

class myBinaryTree:
    def __init__(self, root=None):
        self._root = root

    def add(self, item):
        node = Node(item)
        if not self._root:
            self._root = node
            return
        queue = [self._root]
        while queue:
            cur = queue.pop(0)
            if not cur.lchild:
                cur.lchild = node
                return
            elif not cur.rchild:
                cur.rchild = node
                return
            else:
                queue.append(cur.rchild)
                queue.append(cur.lchild)
    def preorder(self,root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.preorder(root.lchild)
        right_item = self.preorder(root.rchild)
        return result + left_item + right_item

    def inorder(self,root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder(root.lchild)
        right_item = self.inorder(root.rchild)
        return left_item + result + right_item

    def postorder(self,root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.postorder(root.lchild)
        right_item = self.postorder(root.rchild)
        return left_item + right_item + result

# ob = myBinaryTree()
# ob.add(1)
# ob.add(2)
# ob.add(3)
# ob.add(4)
# ob.add(5)
# ob.add(6)
# ob.add(7)
# ob.add(999)
# result = ob.postorder(ob._root)
# print(result)
    
