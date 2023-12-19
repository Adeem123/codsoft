a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c= input("Which action you want to perform: ")

if c == "+":
    print(a + b)

elif c == "-":
    print(a - b)

elif c == "*":
    print(a * b)

elif c == "/":
    print(a / b)

else:
    print("Invalid Input")