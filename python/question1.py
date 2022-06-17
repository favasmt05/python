a=int(input("enter physics mark" ))
b=int(input("enter chemistry  mark" ))
c=int(input("enter biology mark" ))
d=int(input("enter maths mark" ))
e=int(input("enter computer mark"))
total=a+b+c+d+e
per=total*100/500
print("percentage obtained")
if per >= 90:
    print("GRADE A")
elif per>= 80:
    print("GRADE B")
elif per>= 70:
    print("GRADE C")
elif per>= 60:
    print("GRADE D")
elif per>= 40:
    print("GRADE E")
elif per < 40:
    print("GRADE F")
else:
    print("fail")