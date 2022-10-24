arr=[13,42,2,3,6,90,8,23]
def swap(a,b,arr):
    print(a,b)
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp

    
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

quick(0,len(arr)-1,arr)




# def foo(num):
#     if num ==1 or num ==0:
#         return num
#     return foo(num-1)+foo(num-2)


# print(foo(5))

