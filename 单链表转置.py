
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def initListnode(myList=[1,2,3,4,5]):
    head = ListNode(myList[0])
    p = head
    for one in range(1, len(myList)):
        p.next = ListNode(myList[one])
        p = p.next
    return head

def showList(head):
    while head:
        print(head.val)
        head = head.next

def listReversed(head):
    if head is None:
        return None
    head0 = None
    while head:
        p = head.next
        head.next = head0
        head0 = head
        head = p

    return head0

# head = initListnode()
# head_reversed = listReversed(head)  
# showList(head_reversed)  
