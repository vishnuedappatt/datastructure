# a=[(1,3,5),(2,6,9)]
# print(type(a))
# print(a)
# a.append(10)
# print(a)
# a.pop()
# print(a)
# # a[1]=4
# # print(a)
# b=a[1]
# print(b)
# b=list(b)
# print(b)
# b.append(99)
# print(b)
# b=tuple(b)
# a[1]=b
# print(a)


# a=[1,55,33,4,2,100,8]
# for i in range(len(a)-1):
#     for j in range(len(a)-1-i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#         print(a)
# print(a)



a=[1,33,4,23,5,8]
# for i in range(1,len(a)):   
#     temp=a[i]      #
#     j=i-1 
#     while j >=0  and  temp < a[j]:
#         a[j+1]=a[j]
#         j-=1    
#     a[j+1]=temp  
    
# print(a)


v='dskjfhdskfh jfdsbfkdnb dnhfjk'
print(v.split())
b=v.split()
print(b[1])
print(len(b[1]))

print(v[2:3])
v