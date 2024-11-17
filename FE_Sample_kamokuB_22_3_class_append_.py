# FEサンプル問題'22公開　問3

class ListElement:
    def __init__(self,qVal) -> None:
        self.val=qVal
        self.next=None

ListHead = ListElement(None)

def append(qVal):
    prev=ListElement(None)
    curr=ListElement(qVal)
    global ListHead
    if ListHead == None:
        ListHead = curr
    else:
        prev = ListHead
        while prev.next != None:
            prev = prev.next
        prev.next = curr
    
append("あ")
append("い")
append("う")
append("え")
append("お")

print(ListHead.val,ListHead.next.val,ListHead.next.next.val,ListHead.next.next.next.val,ListHead.next.next.next.next.val,ListHead.next.next.next.next.next.val)
