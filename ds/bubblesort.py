list=[1,77,43,222,33,2,8,11,0]
print(list)


length=len(list)
print(length)
for j in range(length-1):
    for i in range(length-1):
        if list[i]>list[i+1]:
            list[i] ,list[i+1]=list[i+1],list[i]
    print(list)
    print(' ----------------  ')
print(list)
    
# list=[1,66,444,5,666,51,0,6,10]   
# length=len(list) 
# print(list)
# for i in range(length-1,1,-1):
#     for j in range(i):
#         if list[j]>list[j+1]:
#             temp=list[j]
#             list[j]=list[j+1]
#             list[j+1]=temp
#         print(list)
#     print('.................')
# print(list)




# n2



