x='*'

def pyr1():
    for i in range(6):
        a=i*x
        print(a)


def pyr2():
    for i in range(6, 0, -1):
        b=i*x
        print(b)

def pyr3():
 
    for i in range(7):
    
        print(i*x)
    for j in range(7,-1,-1):

        print(j*x)

print('-----------------------------------------')
print('               PRINT PYRAMID             ')
print('-----------------------------------------')
print('                                         ')

print("select operation -\n" \
        "1. print half pyramid\n" \
        "2. print inverted half pyramid\n"
        "2. print pyramid\n" )

print('-----------------------------------------')        
A=int(input('select a operation \n'))

if A==1:
    pyr1()
elif A==2:
    pyr2()

elif A==3:
    pyr3()
else:
    print("error")