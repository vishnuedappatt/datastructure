def foo(arr,key):
    left=0
    right=len(arr)-1
    mid=0
    while left <= right:
        mid=(left+right)//2
        mid_num=arr[mid]
        print(mid_num)
        if key ==mid_num:
            return mid
        if mid_num < key:
            print('a',left)
            left=mid+1
            print('b',left)
        else:   
            print('a',right)
            right=mid-1
            print('b',right)
    return -1

a=[1,2,4,6,8,40]
print(foo(a,190))