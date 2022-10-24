


class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def Print(self):
        n=self.head
        if n is None:
            print("empty")
        while n is not None:
            print(n.data,end=' ')
            n=n.ref
            
    def addbegin(self,data):
        new=Node(data)
        # n=self.head
        new.ref=self.head
        self.head=new
        
    def addend(self,data):
        n=self.head
        new=Node(data)
        if n is None:
            self.head=new
        else:       
            while n.ref is not None:
                n=n.ref
            n.ref=new
            self.tail=new
            
 
            

    def after_adding(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:                
                break
            else:
                n=n.ref
        if n is None:
            print('no match')
        else:
            new=Node(data)
            new.ref=n.ref
            n.ref=new
            
            
    def adding_before(self,data,x):
        n=self.head
        while n.ref is not None: 
            if n.ref.data==x:
                break
            else:
                n=n.ref
        if n is None:
            print('no match')
        else:
            new=Node(data)
            new.ref=n.ref
            n.ref=new
            
            
    def reverse(self,PP):
        n=self.head
        while n is not None:       
            PP.addbegin(n.data)  
            n=n.ref
    
    
    # def stack(self):
    #     if self.head is None:
    #         print("empty list")
    #     else:
    #         n=self.head
    #         while n.ref.ref is not None:
    #             n=n.ref
    #         print( 'stack',LL.tail.data)
    #         n.ref = None
    #         self.tail=n
        

    # def Queue(self):
    #     if self.head is None:
    #         print('empty')
    #     else:
    #         n=self.head        
    #         print (KK.head.data)           
    #         self.head=n.ref
            




LL=LinkedList()
LL.addbegin(11)
LL.addbegin(12)
LL.addbegin(161)
LL.addend(98)
LL.addend(18)
LL.addend(1)
LL.addend(2)
LL.addend(3)
LL.addend(4)
LL.Print()

PP=LinkedList()
LL.reverse(PP)
print(' ')
PP.Print()
# LL.stack()
# LL.stack()
# LL.stack()
# LL.Print()
# print(' ')
# print('stack',LL.tail.data)
# LL.stack()



# LL.Print()
# LL.after_adding(22,12)
# LL.adding_before(44,12)
# # print('ddd',LL.tail.data)

# LL.Print()
# PP=LinkedList()
# LL.reverse(PP)
# print('dfdffdf')
# PP.Print()
# PP.stack(11)
# PP.stack(122)
# +971503307554
# PP.stack(788)
# PP.stack(56)
# PP.Print()


# LL.addbegin(11)
# LL.addbegin(13)
# LL.addbegin(555)
# LL.addbegin(78)
# LL.Print()
# LL.Queue()
# LL.Queue()
# LL.Queue()
# LL.Queue()




# Queue

# KK=LinkedList()
# KK.addend(11)
# KK.addend(21)
# KK.addend(121)
# KK.addend(141)
# KK.addend(51)
# KK.Print()
# print('   ')
# KK.Queue()
# KK.Queue()
# KK.Queue()
# KK.Print( )




# LL=LinkedList()
# LL.addbegin(11)
# LL.addbegin(1)
# LL.addbegin(5)
# LL.addbegin(6)
# LL.addbegin(9)
# LL.addbegin(12)
# LL.Print()
# PP=LinkedList()
# LL.reverse(PP)
# PP.Print()
