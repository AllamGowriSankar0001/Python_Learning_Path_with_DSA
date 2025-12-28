# Write a program to find the largest of three numbers using nested if-else.
num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
num3 = int(input("Enter the number 3 : "))

if(num1 > num2):
    if(num1>num3):
        print(f"{num1} is greater than {num2} and {num3}")
    else:
        print(f"{num3} is greater than {num1} and {num2}")
else:
    if(num2>num3):
        print(f"{num2} is greater than {num1} and {num3}")
    else:
        print(f"{num3} is greater than {num1} and {num2}")

