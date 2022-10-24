
def sorted_merge(a,b):
    sorted=[]
    len_a=len(a)
    len_b=len(b)
    i=j=0
    while len_a >i and len_b >j:
        if a[i] <=b[j]:
            sorted.append(a[i])
            i+=1
        else:
            sorted.append(b[j])
            j+=1
    while len_a > i:
        sorted.append(a[i])
        i+=1
    while len_b > j:
        sorted.append(b[j])
        j+=1
        
    return sorted


def merge(arr):
    print(arr)
    if len(arr) <= 1:
        return arr
        
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=merge(left)
    right=merge(right)
    return sorted_merge(left,right)


list1=[2,43,65,2,8,1,66,81,9]
print(merge(list1))








# def sorted_merge(a,b,arr):
#     len_a=len(a)
#     len_b=len(b)
#     i=j=k=0
#     while len_a >i and len_b >j:
#         if a[i] < b[j]:
#             arr[k]=a[i]
#             i+=1
#             k+=1
#         else:
#             arr[k]=a[j]            
#             # sorted.append(b[j])
#             j+=1
#             k+=1
       
#     while len_a > i:
#         arr[k]=a[i]
#         k+=1
#         i+=1
#     while len_b > j:
#         arr[k]=b[j]
#         k+=1        
#         j+=1
        
  


# def merge(arr):
#     print(arr)
#     if len(arr) <= 1:
#         return arr
    
#     mid=len(arr)//2
#     left=arr[:mid]
#     right=arr[mid:]
#     merge(left)
#     merge(right)
#     sorted_merge(left,right,arr)


# list1=[2,43,65,2,8,1,66,81,9,6,0]
# merge(list1)
# print(list1)




