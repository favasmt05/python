
c=[[0,0],[0,0]]

def add(a,b):
    for i in range(len(a)):
        for j in range(len(a[0])):
         c[i][j]=a[i][j]+b[i][j]

    print(c)                                          

def mult(a,b):
    for i in range(len(a)):
        for j in range(len(a[0])):
   
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    print(c)


a=[]
x= [int(input("enter 1st element of first matrix \n"))]
x.append( int(input("enter 2nd element of first matrix \n"))  )
y= [int(input("enter 3rd elements of first matrix \n"))]
y.append( int(input("enter 4th element of first matrix \n"))  )
a.append(x)
a.append(y)

print("the first martrix \n",a)

b=[]
x= [int(input("enter 1st element of second matrix \n"))]
x.append( int(input("enter 2nd element of second matrix \n"))  )
y= [int(input("enter 3rd elements of second matrix \n"))]
y.append( int(input("enter 4th element of second matrix \n"))  )
b.append(x)
b.append(y)

print("the first martrix \n",b)

print()

print("select operation -\n" \
        "1. add\n" \
        "2. mult\n" )
A=int(input('select a operation \n'))

if A==1:
    print(a,'+',b,'=')
    add(a,b)
elif A==2:
    print(a,'*',b,'=')
    mult(a,b)
else:
    print("error")