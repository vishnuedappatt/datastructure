def insertionsort(list):   
    for i in range(1,len(list)):
        current=list[i]
        pos=i
        while list[pos-1]>current and pos>0:
            # 1,0
            list[pos]=list[pos-1]
            pos=pos-1
            # print(list)
        list[pos]=current
        # print(list,'----------')
        # for j in range(len(list-1)):            
        #     if sorted >list[i]:
                
        #         sorted=list[i] 

    
lists=[4,55,7,888,11,33,2,131]

insertionsort(lists)
print(lists)

a='hey'
print(a)
print(id(a))
a=a.replace('e','E')
print(a)
print(id(a))
