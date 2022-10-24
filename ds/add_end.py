class Node():
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_LL(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def add_beginning(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        n = self.head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def after(self,data,x):
        a = self.head
        while a is not None:
            if a.data == x:
                break
            else:
                a = a.ref
        if a is None:
            print("not found")
        else:
            new_node = Node(data)
            new_node.ref = a.ref
            a.ref = new_node 
      

    def before(self,data,x):
        if self.head is None:
            print('empty')
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            else:
                n=n.ref
        if n.ref is None:
            print("node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node       

    def inser_empty(self,data):  
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("not empty")
            
    def sdelete(self):
        if self.head is None:
            print("empty list")
        else:
            self.head = self.head.ref

    def edelete(self):
        if self.head is None:
            print("empty list")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref = None

    def pdelete(self,x):
        if self.head is None:
            print("empty")
            return
        if self.head.data == x:
            self.head = self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            else:
                n=n.ref
        if n.ref is None:
            print("not present")
        else:
            n.ref = n.ref.ref   



        
l1 = LinkedList()
l1.add_beginning(3)
# l1.add_end(32)
l1.print_LL()