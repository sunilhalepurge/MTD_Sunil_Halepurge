class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:

    def __init__(self):
        self.head = None

    def Insert(self, data):
        if self.head is None:
            self.head=Node(data)
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=Node(data)
    
    def delete(self, data):
        if self.head == None:
            print("LL is empty")
        else:
            temp=self.head
            temp1=None
            while temp.next!=None:
                if temp.data==data:
                    temp1.next=temp.next
                    return
                temp1=temp
                temp=temp.next
        
    def traverse(self):
        if self.head is None:
            return
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
s=Stack()
s.Insert(10)
s.Insert(20)
s.Insert(30)
s.delete(20)
s.traverse()
 