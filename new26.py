
def add(x,y):
    print(x+y)


def sub(x,y):
    print(x-y)

def mult(x,y):
    print(x*y)

def div(x,y):
    print(x/y)

print("select operation -\n" \
        "1. add\n" \
        "2. sub\n" \
        "3. mult\n" \
        "4. div\n")
A=int(input('select a operation'))
x=int(input('enter any number'))
y=int(input('enter any number'))

if A==1:
    add(x,y)
    

elif A==2:
    sub(x,y)
    
elif A==3:
    mult(x,y)

elif A==4:
    div(x,y)

else:
    print("error")




