# Movie ticket booking: Calculate the ticket price based on seat class (Silver, Gold, Platinum) and age group (child, adult, senior). 
# Add a weekend surcharge and allow booking multiple tickets in one go. 


print("Silver   | For Child Rs.100 | For adult and Senior Rs.150")
print("Gold     | For Child Rs.200   For adult and Senior Rs.250")
print("Platinum | For Child Rs.300 | For adult and Senior Rs.350")
schild_count = 0
sadult_count = 0
ticket_price = 0
gchild_count = 0
pchild_count = 0
padult_count = 0
gadult_count = 0
gold_count = 0
platinum_count = 0
silver_count = 0
noOfTicket = int(input("Enter the number of ticket :"))
for i in range(noOfTicket):
    book_ticket = input("Enter the ticket you want : ").lower()
    age_group = input("Enter the age group you belong : ").lower()
    if(book_ticket == "silver"):
        if(age_group == "child"):
            schild_count = schild_count + 1
            ticket_price = ticket_price + 100
            silver_count = silver_count + 1
        else:
            sadult_count = sadult_count + 1
            ticket_price = ticket_price + 150
            silver_count = silver_count + 1    
    elif(book_ticket == "gold"):
        if(age_group == "child"):
            gchild_count = gchild_count + 1
            ticket_price = ticket_price + 200
            gold_count = gold_count + 1
        else:
            gadult_count = gadult_count + 1
            ticket_price = ticket_price + 250
            gold_count = gold_count + 1
    elif(book_ticket == "platinum"):
        if(age_group == "child"):
            pchild_count = pchild_count + 1
            ticket_price = ticket_price + 300
            platinum_count = platinum_count + 1
        else:
            padult_count = platinum_count + 1
            ticket_price = ticket_price + 350
            gold_count = gold_count + 1
if(silver_count > 0):
    print("Silver class : ",silver_count)
    print("Ticket price : ",ticket_price)
print("Ticket Price : ", ticket_price)