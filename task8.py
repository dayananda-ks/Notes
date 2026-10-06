# Online shopping cart: Let the user add items by price in a loop until they type "done". 
# Ask for a coupon code and apply a discount if it is valid. Give free delivery
# above Rs.999, otherwise add a delivery charge. Print the final amount.
total = 0
c = "daya1"
discount = 0
delivery  = 50
while(True):
    user = input("Enter the amount or done : ")
    if(user == "done"):
        break
    total = total + int(user) 
coupan = input("Enter the coupan : ")
if(coupan == c ):
    discount = total * 0.10
    total = total - discount
    total = total + delivery
    msg = "coupan applied"
else:
    msg = "coupan is not applied"
if(total > 999):
    total = total - delivery
    msg2 = "free delivery charge"
else:
    msg2 = "delivery charge added"
print("Discount ",msg  )
print("Free delivery :", msg2)
print("Amount : ", total)
