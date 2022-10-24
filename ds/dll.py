class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class Dll:
    def __init__(self):
        self.head = None

    def print_dll(self):
        if self.head is None:
            print("empty")
        else:
            a=self.head
            while a is not None:
                print(a.data, end=" ")
                a=a.nref

    def rprint_dll(self):
        print()
        if self.head is None:
            print("empty")
        else:
            a=self.head
            while a.nref is not None:
                a=a.nref
            while a is not None:
                print(a.data, end=" ")
                a=a.pref

    def insert_e(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("not empty")

    def add_b(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_e(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            a = self.head
            while a.nref is not None:
                a=a.nref            
            a.nref = new_node
            new_node.pref = a

    def add_aftr(self,data,x):
        if self.head is None:
            print("list is empty")
        else:
            a=self.head
            while a is not None:
                if a.data == x:
                    break
                else:
                    a=a.nref
            if a is None:
                print("not found")
            else:
                new_node = Node(data)
                new_node.nref = a.nref
                new_node.pref = a
                if a.nref is not None:
                    a.nref.pref = new_node
                a.nref = new_node

    def add_bfore(self,data,x):
        if self.head is None:
            print("list is empty")
        else:
            a=self.head
            while a is not None:
                if a.data == x:
                    break
                else:
                    a=a.nref
            if a is None:
                print("not found")
            else:
                new_node = Node(data)
                new_node.nref= a
                new_node.pref = a.pref
                if a.pref is not None:
                    a.pref.nref = new_node                    
                else:
                    self.head = new_node
                a.pref = new_node

    def delete_b(self):
        if self.head is None:
            print("cant delete")
            return
        if self.head.nref is None:
            self.head = None
        else:
            a=self.head            
            self.head = a.nref
            self.head.pref = None

    def delete_e(self):
        if self.head is None:
            print("cant delete")
            return
        if self.head.nref is None:
            self.head = None
        else:
            a=self.head
            while a.nref is not None:
                a=a.nref
            a.pref.nref=None

    def delete_byvalue(self,x):
        if self.head is None:
            print("cant delete")
            return
        
        if self.head.nref is None:
            if self.head.data == x:
                self.head=None
            else:
                print("not presemnt")
            return

        if self.head.data == x:            
            self.head = self.head.nref
            self.head.pref = None
            return

        a=self.head
        while a is not None:
            if a.data == x:
                break
            a=a.nref
        
        if a.nref is not None:
            a.nref.pref = a.pref
            a.pref.nref = a.nref
        else:
            if a.data == x:
                a.pref.nref=None
            else:
                print("not present")
       


            





            





dll = Dll()
# dll.print_dll()
dll.insert_e(3)
dll.add_b(8)
dll.add_e(99)
dll.print_dll()

print("______")

dll.add_aftr(111,3)
dll.add_bfore(56,8)
dll.delete_b()
dll.delete_e()
dll.print_dll()
print("______")
dll.rprint_dll()
