# Online shopping cart: Let the user add items by price in a loop until they type "done". 
# Ask for a coupon code and apply a discount if it is valid. Give free delivery
# above Rs.999, otherwise add a delivery charge. Print the final amount.

def cart(name):
    sum = 0
    while(True):
        user = input("Enter the amount or done :")
        if(user == "done"):
            print("Thank you for visiting")
            break
        else:
            sum = sum + int(user)
cart(name=input("Enter the name :"))