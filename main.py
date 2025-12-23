try:
    length = int(input("Enter password length: "))
    if length <= 0:
        print("Password length must be greater than zero")
except ValueError:
    print("Please enter a number")
