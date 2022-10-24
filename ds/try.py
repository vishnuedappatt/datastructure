
# a=[2,43,67,99]
# # # linear
# # def search(a,k):
# #     flag=0
# #     for i in range(len(a)-1):
# #         if k==a[i] :
# #             flag=1
# #             break
# #     if flag== 1:
# #         print('key found',i)
# #     else:
# #         print('no found')
    
# # search(a,978)

# # binary
# def binary(a,k):
#     left=0
#     right=len(a)-1
#     mid=0
#     while left <=right:
#         mid=(left+right)//2
#         mid_num=a[mid]
#         if k==mid_num:
#             return mid
#         if mid_num < k:
#             left= mid+1
#         else:
#             right=mid-1
    
#     return -1
        
# print(binary(a,2))


# bubble
# a=[4,435,24,4432,675,9]

# def bubble(a):
#     for j in range(len(a)-1):
#         for i in range(len(a)-1):
#             if a[i] >a[i+1]:
#                 a[i],a[i+1]=a[i+1],a[i]
                
#         print(a)

# bubble(a)
                
                
                
# selection
# a=[4,34,245,6732,9,0]
# def section(a):
#     for j in range(len(a)-1):
#         for i in range(j,len(a)-1):
#             if a[i] < a[i+1]:
#                 a[i],a[i+1]=a[i+1],a[i]
#         a[j],a[len(a)-1]=a[len(a)-1],a[j]           
            
#     print(a)
        
# section(a)




# insertion
# a=[65,74,4,32,67,1,0]
# # def insertion(a):
#     current=a[0]
#     i=j=0
#     while j>=0 and current < a[i]:        
#         a[j+1]=a[i]
#         j-=1        
#         current=a[i]
#     a[i]=current
#     print(a)
    
# insertion(a)
