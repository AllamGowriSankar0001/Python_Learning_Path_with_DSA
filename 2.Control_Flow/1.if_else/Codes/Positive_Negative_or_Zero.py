# Write a program to check whether a number is positive, negative, or zero using nested if-else.

num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")