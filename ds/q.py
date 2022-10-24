class Node():
    def __init__(self,data):
        self.data=data
        self.ref=None

class Ll():
    def __init__(self):
        self.head = None
    
    def prints(self):
        if self.head is None:
            print("empty")
        else:
            a=self.head
            while a is not None:
                print(a.data, end=" ")
                a=a.ref

    def add_b(self,data):
        new_node = Node(data)
        new_node.ref= self.head
        self.head = new_node

    def rem_dup(self):
        a=self.head
        while a is not None:
            b= a.ref
            while b is not None:
                if a.data == b.data:
                    a.ref = b.ref
                b=b.ref
            a=a.ref


        

l=Ll()
l.add_b(3)
l.add_b(3)
l.add_b(6)
l.add_b(8)
l.add_b(8)
l.add_b(8)
l.rem_dup()
l.prints()