# Parking fee system: Charge by vehicle type (bike, car, truck) and hours parked, with
# a minimum charge for the first hour and a daily maximum cap. Allow multiple
# vehicles until the user exits.

print("Parking Area")
print("Only car, bike and Truck are allowed.for exit (exit)")
bike = 10
car = 20
truck = 30
ca = 0
ba = 0
ta = 0
ct = 1
ctotal_amount = 0
btotal_amount = 0
ttotal_amount = 0
max_cap = 100
total_amount = 0
while(True):
    vehicalType = input("Type of vechical(car/bike/vehical) to exit (exit)  : ").lower()
    if vehicalType == "exit":
        print("Thank you for visting!")
        break
    else:
        time = int(input("Total time : "))
        if(vehicalType == "car"):
            if(time >=1 ):
                ct = 1 * time
                ca = car * ct
                ctotal_amount = total_amount + ca
                if(ctotal_amount > max_cap):
                    ctotal_amount = max_cap
                    print("vehicle : car ")
                    print("totol hour : ",ct)
                    print("amount :", ctotal_amount)
                    ctotal_amount = 0
                    ct = 0
                else:
                    print("vehicle : car ")
                    print("totol hour : ",ct)
                    print("amount :",ctotal_amount)
                    ctotal_amount = 0
        if(vehicalType == "bike"):
            if(time >=1 ):
                ct = 1 * time
                ba = bike * ct
                btotal_amount = btotal_amount + ba
                if(btotal_amount > max_cap):
                    btotal_amount = max_cap
                    print("vehicle : bike ")
                    print("totol hour : ",ct)
                    print("amount :", btotal_amount)
                    btotal_amount = 0
                    ct = 0
                else:
                    print("vehicle : bike ")
                    print("totol hour : ",ct)
                    print("amount :",btotal_amount)
                    btotal_amount = 0

        if(vehicalType == "truck"):
            if(time >=1 ):
                ct = 1 * time
                ba = truck * ct
                ttotal_amount = ttotal_amount + ba
                if(ttotal_amount > max_cap):
                    ttotal_amount = max_cap
                    print("vehicle : Truck ")
                    print("totol hour : ",ct)
                    print("amount :", ttotal_amount)
                    ttotal_amount = 0
                    ct = 0
                else:
                    print("vehicle : Truck ")
                    print("totol hour : ",ct)
                    print("amount :",ttotal_amount)
                    ttotal_amount = 0