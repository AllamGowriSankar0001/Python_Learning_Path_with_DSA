# Write a program using elif that:
# Takes two numbers
# Takes an operator (+, -, *, /)
# Performs the selected operation

num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
operator = input("Enter the Operator: ")
if(operator=="+"):
    print(num1+num2 )
elif(operator == "-"):
    print(num1-num2)
elif(operator == "*"):
    print(num1*num2)
elif(operator == "/"):
    print(num1/num2)