units=float(input("Enter the total units consumed : "))
bill = 0
if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units-100)*1.5
elif units <= 300:
    bill = (100*1.5)+(units-200)*3
else:
    bill = (100*1.5)+(100*3)+(units-300)*5
if bill > 0:
    bill += 50
print("total bill amount is:   Rs", bill)




