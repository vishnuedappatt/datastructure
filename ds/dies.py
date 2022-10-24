# import random


# list=[1,2,3,4,5,6]
# def getvalue():
#     value=random.choice(list)   
#     return value

# getvalue()

# player1=0
# player2=0


# while True:    
#     x=int(input(' choice  1 for player1 2 for player2  3 for quit '))    
#     if x==1:      
#         if player1 <20:           
#             val=getvalue()
#             print(val)
#             if val!=6:
#                 player1=player1+val
#                 if player1 >20:
#                     print('winner')
#                     break
#             print('total score player1',player1)
            
                
#     elif x==2:
#         if player2 <20:         
#             val=getvalue()
#             print(val)
#             if val!=6:
#                 player2=player2+val
#                 if player2 >20:
#                     print('winner2')
#                     break
          
#             print('total score player2',player2)
       
#     elif x==3:
#         break
#     else:
#         print('invalid number')
        

    
    
    
    
    
import random


list=[3,4,2,1,5,6]
def getvalue():
    value=random.choice(list)   
    return value

# getvalue()
# bob=input('enter the player2 name')
# bpp=bob
# print(bob)
# print(bpp)

plr1=input('enter the name of player1  ')
plr2=input('enter the name of player2   ')

player1=0
player2=0
# y=int(input('enter 1 for start the game'))
flag=0
while True:    
    # x=int(input(' choice  1 for player1 2 for player2  3 for quit '))  
      
    if flag==0: 
        print(' ')
        print(f'{plr1}  you can roll the dies enter 1')
        v=int(input(''))
        if v==1:                
            if player1 <20:           
                val=getvalue()
                print( 'you got :',val)
                if val!=6:
                    player1=player1+val
                    flag=1
                    if player1 >=20:
                        print(f'{plr1} is winner')
                        break
                flag=1
                print(f'total score {plr1}',player1)
            
                
    elif flag==1:
        if player2 <20: 
            print(f'{plr2} you can roll the dies enter 2  ')        
            v=int(input(' '))
           
            if v==2:
                val=getvalue()
                print('you got ',val)
                if val!=6:
                    player2=player2+val
                    flag=0
                    if player2 >=20:
                        print(f'{plr2} is winner')
                        for i in range(100):
                            print("**")
                            if i==10 or i==20 or i==30 or i==50:
                                print(f'{plr2} is winner')
                        break
                flag=0
                print(f'total score {plr2} ',player2)

    else:
        print('invalid number')
        

    