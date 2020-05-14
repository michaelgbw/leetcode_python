#coding=utf-8
import sys 
#str = input()
#print(str)
#print('Hello,World!')

class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
          

        
def reverse(head):
    if head is None:
        return None
    head0 = None
    while head:
        p = head.next
        head.next = head0
        head0 = head
        head = p

    return head0


a = ListNode(1,ListNode(2,ListNode(3,None)))
res = reverse(a)
while res :
    print(res.val)
    res = res.next

    


