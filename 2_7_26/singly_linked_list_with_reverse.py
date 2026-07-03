class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList(Node):
    def __init__(self):
        self.head=None
    
    def insertAtBegin(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    
    def insertAtEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=newNode

    def deleteAtBegin(self):
        if self.head is None:
            print("Nothing to remove")
            return
        self.head=self.head.next

    def deleteAtEnd(self):
        if self.head==None:
            print("Nothing to remove")
            return
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None

    def reverse(self):
        self.prev=None
        self.curr=self.head
        self.nex=None
        while self.curr!=None:
            self.nex=self.curr.next
            self.curr.next=self.prev
            self.prev=self.curr
            self.curr=self.nex
        self.head=self.prev

    def display(self):
        if self.head==None:
            print("Nothing to Display")
            return
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
            print()

l=LinkedList()
l.insertAtBegin(2)
l.insertAtBegin(1)
l.insertAtEnd(3)
l.deleteAtEnd()
l.deleteAtBegin()
l.display()
l.reverse()
l.display()