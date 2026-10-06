days = int(input("Enter the number of days : "))
book_price = float(input("Enter the book price : "))
fine = 0
for i in range(1, days + 1):
    if i > 21:
        fine += 5
    elif i > 14:
        fine += 2
if fine > book_price:
    fine = book_price
print("Total Fine : ", fine)
