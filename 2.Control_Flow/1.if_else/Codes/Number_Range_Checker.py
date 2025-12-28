#Write a program to check whether a number lies:
# Between 1 and 100
# Less than 1
# Greater than 100

num = int(input("Enter the Number: "))
if(num<1):
    print("the number is less than 1")
else:
    if(num>1 and num<100):
        print("Number is Between 1 and 100")
    else:
        print("Number is greater than 100")