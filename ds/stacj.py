from hashlib import new


class Node:
    def __init__(self,data) :
        self.data=data
        self.ref=None
        
class LL:
    def __init__(self) :
        self.head=None
        self.tail=None
        
    def PrintL(self):
        n=self.head
        if n is None:
            print('emptyqq')
        else:
            while n is not None:
                print(n.data,end=' ')
                n=n.ref
                
    def addBegin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
        
    def stack(self):
        n=self.head
        if n is None:
            print('empty')
        else:           
            print(n.data,'dd')
            self.head=n.ref
    def quee(self):
        n=self.head
        if n is None:
            print('emptiii')
        else:
            while n.ref.ref is not None:
                n=n.ref                
            print(n.ref.data)
            n.ref=None
            
    def addafter(self,data,x):
        new_node=Node(data)
        n=self.head
        if n.data==x:
            print('dd')
            new_node.ref=n.ref
            n.ref=new_node
            
        else:
            
            while n.ref is not None:
                if n.data ==x:
                    new_node.ref=n.ref
                    n.ref =new_node
                    break
                else:
                    n=n.ref
    def addbefore(self,data,x):
        n=self.head
        new_node=Node(data)
        if n.data ==x:
            print('jj')
            new_node.ref=self.head
            self.head=new_node
        else:
            while n.ref is not None:
                if n.ref.data==x:
                    new_node.ref=n.ref
                    n.ref=new_node
                    break
                else:
                    n=n.ref
        
        
l1=LL()
l1.addBegin(2)
l1.addBegin(1)
l1.addBegin(5)
l1.addBegin(4)
l1.addBegin(9)

l1.PrintL()
l1.addafter(10,9)
print()
l1.PrintL()
l1.addbefore(11,9)
print()
l1.PrintL()