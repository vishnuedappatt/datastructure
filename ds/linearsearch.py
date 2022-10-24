
list=[1,33,4,6,23,66,99]
def search(key):
    l=len(list)-1
    for i in range(l):
        if key ==list[i]:
            print('key present',i)
    print('key not prest')


print(list)
key=int(input('enter key'))
search(key)