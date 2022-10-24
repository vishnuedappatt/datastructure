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

    

    def add_end(self,data):
        n = self.head
        new_node = Node(data)
       
        if self.head is None:
            self.head = new_node
        else:
            while n.ref is not None:
                
                n = n.ref
            n.ref = new_node

    def arrays(self,arr):
        l=LinkedList()
        a=0
        while a<len(arr):            
            l.add_end(arr[a])            
            a+=1
            
        l.print_LL()

l1 = LinkedList()
arr=[2,4,5,6,3,5,8]
l1.arrays(arr)
