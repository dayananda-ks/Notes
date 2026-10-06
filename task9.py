# Login system: Check a username and password with a limit of 3 attempts, and lock
# the account after 3 failures. On success, show a role-based menu (admin or user).
adminName = "daya"
apass = "123"
userName = "abc"
upass = "123"
n = 3
i = 1
while(n + 1 > i ):
    name = input("Enter the name : ").lower()
    password = input("Enter the Password : ").lower()
    if(name == adminName) and (password == apass):
        print("\n=== ADMIN MENU ===")
        print("1.View System Logs")
        print("2.Manage Users")
        print("3.Logout")
        break
    elif (name == userName)  and (upass == upass):
        print("\n=== USER MENU ===")
        print("1.View Profile")
        print("2.Edit Settings")
        print("3.Logout")
        break
    else:
        if( i == 3):
            print("No more attempts.")
            print("Account Locked.")
            i = i + 1
        else:
            print("Wrong password and username.",n - i," attempts is there.")
            i = i + 1

