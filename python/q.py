 
units = float(input(" enter Number of Units you Consumed : "))
if(units <= 50):
    amount = units * .50
elif(units<=150):
    amount = units * .75
elif(units<=250):
    amount = units * 1.20
elif(units>250):
    amount = units * 1.50
surcharge = float(amount%20)
total = amount + surcharge
print(total)

 