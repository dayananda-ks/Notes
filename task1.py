# from datetime  import datetime
# now = datetime.now()
# print(now)

# import time
# n = 10
# i = 1
# while(n >= i):
#     print("Hello",i)
#     i = i +1
#     time.sleep(0.1)




# check if the number is leap or not using user define function


# def checkYear(year):
#     leap = False
#     if((year % 4 == 0 and year % 100 !=100) or  year % 400 == 0):
#         leap = True
#     return leap
# year = int(input("enter the year : "))
# print(checkYear(year))

# These problems force you to handle overlapping logical rules and subtle edge cases.
# • Problem 1: The Balanced Multiplexer
# Write a function evaluate_numbers(a, b). If both numbers are even, return the smaller number. If both numbers are odd, return their sum. If one is even and one is odd, 
# return their absolute difference.

# def ev_num(n1,n2):
#     return f"{n1} is greater" if n1 > n2 else f"{n2} is greater"
# print(ev_num(n1 = int(input("Enter the number : ")), n2 = int(input("Enter the number : "))))

# • Problem 2: Word Boundary Matching
# Write a function clean_match(text). Given a string of words separated by spaces, return True if all words start with the exact same alphanumeric character
#  (case-insensitive) and the string contains at least two words. Otherwise, return False.
# • Problem 3: Coupon Eligibility Matrix
# Write a function can_apply_discount(cart_total, is_member, has_coupon). A discount applies if:
# 	1. The cart_total is $100 or more, OR
# 	2. The user is_member and has a total over $50, OR
# 	3. The user has_coupon regardless of total, unless they are a non-member with a total under $20.

# def clean_match(text):
#     result = False
#     text_len = len(text)
#     if(len(text) == 2):
#         result = True
#     for i in range((text_len//2)):
#         if(text[i] == text[(text_len // 2) + 1]):
#             result = True
#     else:
#         result = False
#     return result
# print(clean_match(text="Hello4 Hello4"))

# Hotel menu and billing: Display a menu with Idli (Rs.30), Dosa (Rs.50), Biryani (Rs.180),
# and Coffee (Rs.20), plus an option to generate the bill. Let the customer keep ordering items
# and quantities until they choose to generate the bill. Reject invalid choices. Apply a 10%
# discount if the subtotal exceeds Rs.500, then add 5% GST and print the final bill.

# algo
# display the menu with price
def foodOrder(customer):

    print("1.Idli : 30\n2.Dosa : 50\n3.Biryani : 180\n4.cofee : 20\n5.Genarate Bill")
    # customer only choose these options
    # customer ordering items untill they choose bill.
    #intitaly total amount, each food amount, quantity is 0. we need to intitlize it has 0.
    # use while loop bcz user decide how many time they order we don't know that
    # using condtinal statement it calc each food quantity and amount.
    # user used 1 2 3 4 5 for food order bcz validation purpose
    idli_quantity = 0
    dosa_quantity = 0
    coffee_quantity = 0
    biryani_quantity = 0
    ia = 0
    ba = 0
    da = 0
    ca = 0
    ip = 30
    dp = 50
    bp = 180
    cp = 20
    gst = 0
    discount = 0
    total_amount = 0
    while(True):
        order = int(input("Enter the food : "))
        if(order > 5 ) or (order <= 0):
            print("Choose only 1 to 5 options")
        elif(order == 1):
            idli_quantity = idli_quantity + 1
            # idli amount
            ia = ia + ip
            total_amount = total_amount + ia
        elif(order == 2):
            dosa_quantity = dosa_quantity + 1
            da = da + dp
            total_amount = total_amount + da
        elif(order == 3):
            biryani_quantity = biryani_quantity + 1
            ba = ba + bp
            total_amount = total_amount + ba
        elif(order == 4):
            coffee_quantity = coffee_quantity + 1
            ca = ca + cp
            total_amount = total_amount + ca
        elif(order == 5):
            if(total_amount <=  0):
                print("You not yet order.. order the food ")
                continue
            else:
                print("==== bill ====")
                print("Customer : ",customer)
                print("Items | quantity | Amount")
                if(idli_quantity > 0):
                    print("Idli     ", idli_quantity,   "        " , ia)
                if(dosa_quantity > 0):
                    print("Dosa     ", dosa_quantity,   "        " , da)
                if(biryani_quantity > 0):
                    print("Biryani  ", biryani_quantity,"        " , ba)     
                if(coffee_quantity > 0):
                    print("Coffee   ", coffee_quantity, "        " , ca)
                discount = total_amount * 0.10
                total_amount = total_amount - discount
                gst = total_amount * 0.05
                print("Total amount : ", total_amount + gst)
                print("Thank you for visting!")
                break
foodOrder("Daya")
foodOrder("Ashu")