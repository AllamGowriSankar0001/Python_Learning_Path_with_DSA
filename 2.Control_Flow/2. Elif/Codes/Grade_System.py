# Write a program using if-elif-else to display grades:
# Marks ≥ 90 → A
# Marks ≥ 75 → B
# Marks ≥ 60 → C
# Marks ≥ 40 → D
#Marks < 40 → Fail

num = int(input("Enter a Number: "))
if(num>=90):
    print("your grade is A")
elif(num<90 and num>=75):
    print("your grade is B")
elif(num<75 and num>=60):
    print("your grade is C")
elif(num<60 and num>=40):
    print("your grade is D")
else:
    print("your failed")