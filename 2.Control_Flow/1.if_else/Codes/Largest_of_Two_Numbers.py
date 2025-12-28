# Write a program to find the largest of two numbers entered by the user.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is the largest number than {num2}")
else:
    print(f"{num2} is the largest number than {num1}")
