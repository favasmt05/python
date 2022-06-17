num = int(input("Enter a number: "))
fact= 1
if num < 0:
    print("factorial dose not exist" )
elif num == 0:
    print("factorial of zero is 1") 
else: 
    for i in range(1,num + 1): 
        fact = fact*i
print("The factorial of",fact)    