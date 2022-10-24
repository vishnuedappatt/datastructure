


# list=[100,4,55,7,888,11,33,2,131,1]
# print(list)
# # min= list[0]
# for j in range(len(list)-1):
#     for i in range(j+1,len(list)):
#         min=list[j]
#         print(min,'minn')
#         if min >list[i]: 
#             min=list[i]            
#         print(min,'hopp')
#         min_index=list.index(min)     
#         list[j],list [min_index]=list[min_index],list[j]
#         print(list)
#     print(list)
    
    

# for j in  range(len(a)-1):
#     for i in range(len(a)-1):
#         min=a[j]
#         if min > a[i]:
#             min=a[i]
#     print(min,'d')  
    
#     print(a)


# a=[11,3,4,6,7,1,90]
# for j in range(len(a)-1):    
#     print(j,'ddddddddddd')
#     min=a[j]   
#     for i in range(j+1,len(a)-1):  
#         if min > a[i]:
#             min=a[i]
#         print(min,'off',j,i)
#         print(i,j)
#         a[j],a[i]=a[i],a[j]
#         print(a)



# a=[11,3,4,6,7,1,90]
# for i in range(1,len(a)):
#     j=i-1  #small
#     current= a[i]     #big
#     while j>=0  and current < a[j]:
#         print(current)
#         print(a)
#         a[j+1]=a[j]
#         j-=1
#     print(j)
#     a[j+1]=current
# print(a)

# a=[9,54,2,1,3]
# for i in range(1,len(a)):
#     current=a[i]
#     j=i-1    
#     while j >=0 and current < a[j]:
#         a[j+1]=a[j]
#         j-=1
#     a[j+1]=current
    
# print(a)


# Quick sort
# a=[9,37,28,92,0,2]

# def swap(a,b,arr):
#     arr [a],arr[b]=arr[b],arr[a]

    

# def partition(arr,start,end):
#     pivet_index=start
#     pivot=arr[pivet_index]  
#     while start < end :
#         while  start <len(arr)  and arr[start] <= pivot:
#             start +=1
#         while arr [end] > pivot:
#             end -=1
#         if start < end:
#             swap(start,end,arr)
#     swap(pivet_index,end,arr)
#     return end


# def quick_sort(a,start,end):
#     if start <end:
#         endId=partition(a,start,end)
#         quick_sort(a,start,endId-1)
#         quick_sort(a,endId+1,end)
        
#         print(a)


# quick_sort(a,0,len(a)-1)





# a=[1,33,4,6,3,76,90]
# def swap(a,b,arr):
#     arr[a],arr[b]=arr[b],arr[a]
    
# def partition(arr,start,end):
#     pivot_index=start
#     pivot=arr[pivot_index]
#     while start < end:
#         while arr[start] < pivot:
#             start +=1
#         while arr[end] >pivot:
#             end -=1
#         if start < end:
#             swap(start,end,arr)
#     swap(pivot_index,end,arr)
#     return end
            
# def quick(a,start,end):
#     if start< end:
#         id=partition(a,start,end)
#         quick(a,start,id-1)
#         quick(a,id+1,end)
#     print(a)


# insertion
# a=[1,33,4,6,3,76,90]
# for i in range(1,len(a)):
#     current=a[i]
#     j=i-1
#     while j>=0 and current <a[j]:
#         a[j+1]=a[j]
#         j-=1
#     a[j+1]=current
# print(a)



# selection
# a=[1,22,43,5,67]
# for i in range(len(a)-1):
#     min=a[i]
#     for j in range(i+1,len(a)-1):      
#         if min > a[j]:
#             min=a[j]
#             print(min)
#             a[i],a[j]=a[j],a[i]
# print(a)

# quick

arr=[13,42,2,3,6,90,8,23]
def swap(a,b,arr):
    # if a !=b:
    print(a,b)
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp
    # print(arr,'start')
    # arr[a],arr[b]=arr[b],arr[a]
    # print(arr,'last')
    
    
    
def partition(start,end,arr):
    pivot_index=start
    pivot=arr[pivot_index]
    while start < end :
        while len(arr) > start and arr[start] <= pivot :
            start +=1
        while arr[end] > pivot:
            end-=1
            
        if start < end:
            swap(start,end,arr)
    swap(pivot_index,end,arr)
    return end

def quick(start,end,arr):
    if start < end:
        value=partition(start,end,arr)      
        quick(start,value-1,arr)
        quick(value+1,end,arr)
    print(arr,'kk')
    
quick(0,len(arr)-1,arr)