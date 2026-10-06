# Employee registration: Accept an employee's name and age, and keep asking for the age
# until it is between 18 and 60. Let the user choose a department (Development, Testing, HR, or
# Sales), each with a different base salary. Add an experience bonus (0- 1 years: none, 2-4 years:
# Rs.7000, 5+ years: Rs.15000). Print the registration summary


#logic
# take emolpyee name first then take age if age is lessthan 18 and greater than 60. keep asking until  user enter between that number. while loop for age if age is valid then only continue.
# after choose the deapartment we display the which are the department is there then select only onr of that. each with diff base slry
# after selecting department, each dep has base sal. employe must enter there exp based on exp bonus will add initial 0 to 1 there is no bonus.employee_name = input("Enter the Name : ")
employee_name = input("Enter the Name : ")
dev_sal = 45000
test_sal = 35000
hr_sal = 30000
sale_sal = 25000

while True:
    employee_age = int(input("Enter the Age : "))
    if employee_age < 18 or employee_age > 60:
        print("Enter the age between 18 to 60")
    else:
        print("Eligible")
        break

print("1.Development")
print("2.Testing")
print("3.HR")
print("4.Sales")

choose_dep = int(input("Choose the department : "))

if choose_dep == 1:
    exp = int(input("Enter your experience : "))
    if exp >= 2 and exp <= 4:
        dev_sal = dev_sal + 7000
    elif exp >= 5:
        dev_sal = dev_sal + 15000
    print("Base Sal :", 45000)
    print("Salary + Bonus : ", dev_sal)

elif choose_dep == 2:
    exp = int(input("Enter your experience : "))
    if exp >= 2 and exp <= 4:  
        test_sal = test_sal + 7000
    elif exp >= 5:
        test_sal = test_sal + 15000
    print("Base Sal : ", 35000)
    print("Salary : ", test_sal)

elif choose_dep == 3:
    exp = int(input("Enter your experience : "))
    if exp >= 2 and exp <= 4:  
        hr_sal = hr_sal + 7000
    elif exp >= 5:
        hr_sal = hr_sal + 15000
    print("Base Sal :", 30000)
    print("Salary : ", hr_sal)

elif choose_dep == 4:
    print("Sales")
    exp = int(input("Enter your experience : "))
    if exp >= 2 and exp <= 4:  
        sale_sal = sale_sal + 7000
    elif exp >= 5:
        sale_sal = sale_sal + 15000
    print("Base Sal : ", 25000)
    print("Salary : ", sale_sal)
