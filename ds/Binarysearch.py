# m=int(input('enter range'))
# list=[int(input('enter values')) for i in range(m)]
# key=int(input('enter key to find'))



# def binarysearch(list,key):
#     low=0
#     high=len(list)-1
#     mid=(high-low)//2
#     print(mid)
#     while low <= high: 
#         if key==list[mid]:
#             print(' index is ',mid)
#             break
#         elif(key>list[mid]):
#             print('value present in right sub section')
#             mid=mid+1
#         else:
#             mid=mid-1
#             print('value present in left sub section')
#     return -1

# list=[1,6,7,8,9,33,55,82,90]
# key=2222

# binarysearch(list,key)

# log(n)



def binary(arr,start,end,key):
    if start<end:
        mid=start+(end-start)//2        
        if key==arr[mid]:
            return mid
        elif(key>=arr[mid]):
            start=mid+1
            return binary(arr,start,end,key)
        elif(key<=arr[mid]):
            start=mid-1
            return binary(arr,start,end,key)
        else:
            return -1        
    return -1   
arrays=[3,4,77,8,1,33,6]
star=0
end=len(arrays)-1

val=binary(arrays,star,end,363)
print(val)

     