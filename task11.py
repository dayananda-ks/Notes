# Multi-floor elevator simulation: Take the current floor and a series of floor requests ending with 0.
#  Move the elevator one floor at a time using loops. 
# Print each floor passed and stop at requested floors. Handle direction changes, ignore the current
# floor, and reject floors above 10.

current_floar = int(input("Enter the current floar : "))
while(True):
    dest_floar = int(input("Enter the dest floar : "))
    if(dest_floar == 0):
        print("Current floar is ",current_floar)
        break
    if(current_floar > 10 or current_floar < 0) or  (dest_floar > 10 or dest_floar < 0):
        print("invalid floars number. Enter the valid floars")
    elif(dest_floar == current_floar):
        print("Currently in your destination floar")
    else:
        if(current_floar < dest_floar):
            for i in range(current_floar,dest_floar + 1):
                print("floar ",i)
            print("Stoped the floar",current_floar)
        else:
            while(current_floar >= dest_floar):
                print("passing floar ", current_floar)
                current_floar = current_floar - 1
            print("Stoped the floar",current_floar)
