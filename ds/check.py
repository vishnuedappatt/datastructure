# tup= (5, 7, 22, 97, 54, 62, 77, 23, 73, 61)
# newtuple = list(map(lambda x: x+3 , [2,3,3])) 
# print(newtuple)
def voo(y):
    return y+2*y
new=list(map(voo,[1,1,1]))
print(new)

