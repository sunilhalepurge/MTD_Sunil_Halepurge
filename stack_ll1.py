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
        else:
            temp1=self.head
            temp=Node(data)
            temp.next=temp1
            self.head = temp
          
    def delete(self):
        if self.head == None:
            print("LL is empty")
        else:
            temp=self.head
            self.head=temp.next
        

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
s.delete()
s.delete()
s.traverse()
 