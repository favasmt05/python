x=float(input("Enter your unit charge"))
if x<=50:
    print(x*.50)
elif x<=150:
    print(x*.75)
elif x<=250:
    print(x*1.20)
elif x>250:
    print(x*1.50)